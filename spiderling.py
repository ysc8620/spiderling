# -*- coding: utf-8 -*-
__author__ = 'ShengYue'
from lxml import etree
from model.db import db
from model.curl import curl
from model.match import match
from model.log import log
import re
import time
i = 1
'''
爬虫
'''
class spiderling:

    def __init__(self, config):
        self.i = 0
        try:
            configtree = etree.ElementTree(file=config)

            # 获取网站属性
            sites = configtree.xpath('//site')
            site = sites[0]
            self.url = site.get('url')


            self.site_name = site.get('siteName')
            self.daily = float(site.get('daily'))
            self.log = site.get('log')
            self.errlog = site.get('error')

            self.linkRule = configtree.xpath('//linkRules/rule')
            self.infoUrlRule = configtree.xpath('//urlRules/rule')
            self.infoRule = configtree.xpath('//targets/target/model/field')

        except:
            log.write('error.log', u'配置文件读取错误')

        self.db = db()

    def run(self, url):
        #休息时间
        time.sleep(self.daily)

        if url == None:
            info = self.db.get_url(self.site_name)

            if info == None:
                log.write(self.log, u'网站读取完成')
                return 0;

            self.db.update_url(info[0])
            url = info[1]

        gurl = curl()
        html = gurl.read(url)
        try:
            if html.strip() == '':
                s = None;
                self.run(s)

        except Exception, e:
            log.write(self.log, url+u' html 获取失败'+Exception+e)
            s = None;
            self.run(s)

        #print html
        self.xtree = match(html, url)
        links = self.xtree.get_all_links(self.linkRule, self.url)

        '''把获取到的连接持久化'''
        for link in links:

            if self.db.check_url(link) == 0:
                self.db.add_url(link, self.site_name)

        '''如果当前连接是详细页则正则所需内容'''
        #for infoxpath in self.infoRule:
        #self.xtree.get_match_info(self.infoRule)

        regInfoLink = re.compile(self.infoUrlRule[0].get('value'))

        if regInfoLink.match(url) <> None:
            self.i = self.i+1
            data = self.xtree.get_match_info(self.infoRule, url)

            self.db.addData(data)
#
#            file_object = open(str(self.i)+'id.txt', 'w')
#            file_object.write(json.dumps(data))
#            file_object.close()
#
            #print json.dumps(data)
        else:
            print u'不是详细也不需要解析'
        s = None
        self.run(s)

    def close(self):
        try:
            self.xtree.close()
        except:
            pass
        try:
            self.db.close()
        except:
            pass



sp = spiderling('cate.xml')

#return
sp.run(sp.url)
#sp.run('http://www.ffdy.cc/movie/35622.html')
sp.close()

#import sqlite3 #导入模块
#cx = sqlite3.connect("d:\\test.db")
#
#cu=cx.cursor()
##cu.execute("""create table catalog ( id integer primary key, pid integer, name varchar(10) UNIQUE )""")
##
##cu.execute(u"insert into catalog values(2, 0, '哈哈')")
##cu.execute(u"insert into catalog values(3, 0, '我是中国')")
##cx.commit()
#
#cu.execute("select * from catalog")
#d =  cu.fetchall()
#for s in d:
#    print s[2]
#cu.close()
#cx.close()