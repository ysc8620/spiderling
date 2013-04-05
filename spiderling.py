# -*- coding: utf-8 -*-
__author__ = 'ShengYue'
from lxml import etree
from model.db import db
from model.curl import curl
from model.match import match
#import model.*
import re

'''
爬虫
'''
class spiderling:

    def __init__(self, config):
        configtree = etree.ElementTree(file=config)

        site = configtree.xpath('//site')
        self.url = site[0].get('url')
        self.site_name = site[0].get('siteName')

        self.linkRule = configtree.xpath('//linkRules/rule')
        self.infoUrlRule = configtree.xpath('//urlRules/rule')
        self.infoRule = configtree.xpath('//urlRules/rule')

        #print self.linkRule[0].get('value')
        self.db = db()

    def run(self, url=None):
        if url == None:
            url = self.db.get_url(self.site_name)
            if url == None:
                print u'爬虫完成'
                return 0;

        gurl = curl()
        html = gurl.read(url)
        #print html
        self.xtree = match(html, url)
        links = self.xtree.get_all_links(self.linkRule, self.url)

        '''把获取到的连接持久化'''
        for link in links:
            if self.db.check_url(link) == 0:
                self.db.add_url(link, self.site_name)

        '''如果当前连接是详细页则正则所需内容'''
        regInfoLink = re.compile(self.url+self.infoRule[0].get('value'))
        if regInfoLink.match(url) <> None:
            print u'是详细页需要解析'
            self.xtree.get_match_info(self.infoRule, self.url)
        else:
            print u'不是详细也不需要解析'

    def close(self):
        self.xtree.close()
        self.db.close()



sp = spiderling('cate.xml')
sp.run(sp.url)
sp.run('http://www.ffdy.cc/movie/35620.html')
sp.close()