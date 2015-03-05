#!/usr/bin/python
#coding=utf-8

import sys,os
reload(sys)
sys.setdefaultencoding('utf8')

from scrapy.selector import Selector
# from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
# from spider.items import DealItem
# from scrapy.utils.response import get_base_url
# import urlparse
import time
# import re
from spider.tools.common import *
from spider.tools.matchfield import *
from spider.tools.db import DB
from spider.tools.redisdb import redisDB


class DmozSpider(CrawlSpider):
    name = 'dmoz'
    xml = None
    allowed_domains = []
    start_urls = []
    website_url = ''
    website_id = 0
    rules = ()
    db = None
    start_time = None
    def __init__(self, *a, **kw):
        new_name = ''
        # 爬虫起始时间
        self.start_time = int(time.time())
        if len(sys.argv) > 3:
            new_name = sys.argv[3].replace('n=','')
        infile = os.getcwd()+r'/spider/spiders/website/' + new_name
        if os.path.exists(infile):
            logs(time.strftime("======%Y-%m-%d %H:%M:%S Spider") +' ' + new_name + ' Start Read.')
            str = file(infile,"a+").read()
            self.xml = Selector(text=str, type='xml')
        else:
            logs(time.strftime("------%Y-%d-%d %H:%M:%S ") +' ' + new_name +' No Exits.')
            exit(0)
        new_name = new_name.replace('.xml','')
        self.name = self.name +':'+ new_name

        # 设置运行域名
        self.allowed_domains.append(self.xml.xpath("//site/@url").extract()[0].strip())
        self.website_url = self.xml.xpath("//site/@url").extract()[0].strip()
        self.db = DB()
        self.website_id = self.xml.xpath("//site/@website_id").extract()[0].strip()
        # 设置起始URL
        start_url = self.xml.xpath("//site/startUrls/url/@url").extract()
        if start_url:
            for url in start_url:
                self.start_urls.append(url.strip())

        # 设置链接规则
        url_rule = self.xml.xpath("//site/queueRules/rule").extract()
        rules = []
        for str in url_rule:
            sl = Selector(text=str, type='xml')
            str_allow = sl.xpath("//rule/@rule").extract()
            str_allow = '' if len(str_allow)<1 else str_allow[0].strip()
            str_deny = sl.xpath("//rule/@deny").extract()
            str_deny = '' if len(str_deny)<1 else str_deny[0].strip()
            str_callback = sl.xpath("//rule/@callback").extract()
            str_callback = '' if len(str_callback)<1 else str_callback[0].strip()

            if str_callback != '':
                if str_deny != '':
                    ru = Rule(LinkExtractor(allow=r""+str_allow, deny=r""+str_deny),callback=str_callback)
                else:
                    ru = Rule(LinkExtractor(allow=r""+str_allow), callback=str_callback)
            else:
                if str_deny != '':
                    ru = Rule(LinkExtractor(allow=r""+str_allow ,deny=r""+str_deny))
                else:
                    ru = Rule(LinkExtractor(allow=r""+str_allow))
            rules.append(ru)
        self.rules = tuple(rules)

        # 初始化redis
        reds = redisDB()
        reds.flushSpider(new_name)

        # 执行初始化
        super(DmozSpider, self).__init__(*a, **kw)
        self._compile_rules()

    def parse_item(self, response):
        item = match_dmoz_field(response=response,xml=self.xml)
        return item

    u''' 爬虫结束时操作 会反馈真实停止状态 '''
    def closed(self,reason):
        # print ===finished+++++
        ''' 自然完成后更新隐藏信息 '''

        logs(time.strftime("======%Y-%m-%d %H:%M:%S Spider ")  +' '+ self.name + ' Stop.')

        weibsite_id = self.website_id

        if reason == 'finished':
            u'隐藏过期商品'
            self.db.execute("UPDATE le_goods SET isshow=0 WHERE uptime<%s AND website_id=%s", [self.start_time, weibsite_id])
            u'显示没过期商品'
            self.db.execute("UPDATE le_goods SET isshow=1 WHERE uptime>%s AND website_id=%s", [self.start_time, weibsite_id])
            self.db.close()
            pass
