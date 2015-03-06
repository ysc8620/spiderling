#!/usr/bin/python
#coding=utf-8

import sys,os
reload(sys)
sys.setdefaultencoding('utf8')

from scrapy.utils.spider import iterate_spider_output
from scrapy.selector import Selector
from scrapy.http import Request, HtmlResponse
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
    is_read_once = False
    def __init__(self, n=None, *a, **kw):
        # 爬虫起始时间
        self.start_time = int(time.time())
        if n == None:
            logs(time.strftime("------%Y-%d-%d %H:%M:%S ") +' Spider Name No Exits.')
            exit(0)
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

        is_read_url = self.xml.xpath("//site/@is_read_url").extract()[0].strip()
        if is_read_url:
            self.is_read_once = True

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

    #################每次初始化读取现有链接#################
    def _requests_to_follow(self, response):
        if not isinstance(response, HtmlResponse):
            return

        if self.is_read_once:
            links = get_all_url(self.website_id)

            for n, rule in enumerate(self._rules):
                for link in links:
                    r = Request(url=link['url'], callback='parse_item')
                    r.meta.update(rule=n, link_text='old page')
                    yield rule.process_request(r)
            self.is_read_once = False

        seen = set()
        for n, rule in enumerate(self._rules):
            links = [l for l in rule.link_extractor.extract_links(response) if l not in seen]
            if links and rule.process_links:
                links = rule.process_links(links)
            for link in links:
                seen.add(link)
                r = Request(url=link.url, callback=self._response_downloaded)
                r.meta.update(rule=n, link_text=link.text)
                yield rule.process_request(r)

    def parse_item(self, response):
        item = match_dmoz_field(response=response,xml=self.xml)
        return item

    u''' 爬虫结束时操作 会反馈真实停止状态 '''
    def closed(self,reason):
        # print ===finished+++++
        ''' 自然完成后更新隐藏信息 '''

        logs(time.strftime("======%Y-%m-%d %H:%M:%S Spider ")  +' '+ self.name + ' Stop.')

        #weibsite_id = self.website_id

        if reason == 'finished':
            u'隐藏过期商品'
            self.db.execute("UPDATE le_goods SET isshow=0 WHERE uptime<%s AND website_id=%s AND isshow=1", [self.start_time, self.website_id])
            #u'显示没过期商品'
            #self.db.execute("UPDATE le_goods SET isshow=1 WHERE uptime>%s AND website_id=%s AND isshow=0", [self.start_time, self.website_id])
            self.db.close()
            pass
