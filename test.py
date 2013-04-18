# -*- coding: utf-8 -*-
__author__ = 'ShengYue'
from lxml import etree
from model.db import db
from model.curl import curl
from model.match import match
import re
import time
import lxml
i = 1
'''
爬虫
'''
class spiderling:

    def __init__(self, config):
        self.i = 0
        configtree = etree.ElementTree(file=config)

        site = configtree.xpath('//site')
        self.url = site[0].get('url')
        self.site_name = site[0].get('siteName')

        self.linkRule = configtree.xpath('//linkRules/rule')
        self.infoUrlRule = configtree.xpath('//urlRules/rule')
        self.infoRule = configtree.xpath('//targets/target/model/field')


        #print self.linkRule[0].get('value')
        self.db = db()

    def run(self, url):

        time.sleep(0.3)
        if url == None:
            info = self.db.get_url(self.site_name)

            if info == None:
                print u'爬虫完成'
                return 0;

            self.db.update_url(info[0])
            url = info[1]

        gurl = curl()
        html = gurl.read(url)

        try:
            if html.strip() == '':
                s = None;
                self.run(s)

        except:
            s = None;
            self.run(s)



        #print html
        self.xtree = match(html, url)
        d = self.xtree.etree.xpath("//div[@class='filmcontents']")
        sd = etree.tostring(d[0],encoding="utf-8",method="html")
        sd = sd.strip()
        print sd
        print '================================='
        reg = re.compile(r'<[!/]?\b(?!(\bpre\b|\bli\b|\bp\b|\bbr\b))+\b\s*[^>]*>|[\s\r\n\t]+')
        ds = reg.sub(' ',sd).strip()
        print ds
        return
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

            print u'是详细页需要解析', str(self.i)
            data = self.xtree.get_match_info_test(self.infoRule, url)
            print u'插入数据', url
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
        self.xtree.close()
        self.db.close()



#sp = spiderling('cate.xml')
#sp.run(sp.url)
#sp.run('http://www.ffdy.cc/movie/35622.html')
#sp.close()

url = 'http://www.dytt8.net/html/gndy/dyzz/20130407/41866.html'
curls = curl()
html = curls.read(url,{})
xtree = match(html, url)
content = xtree.etree.xpath('//div[@id="Zoom"]')

infohtml = lxml.etree.tostring(content[0],encoding="utf-8",method="html")
infohtml = infohtml.strip()
reg = re.compile(r'<[!/]?\b(?!(\bpre\b|\bli\b|\bp\b|\bbr\b|\bspan\b|\bimg\b|\ba\b))+\b\s*[^>]*>')
infohtml = reg.sub(' ',infohtml).strip()

pattern = re.compile(r'◎年　　代　([^<]*)')
ds= pattern.search(html)
print
if(ds==[]):
    print u'找不到'
else:
    print ds[0]

print infohtml
