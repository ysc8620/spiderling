#!/usr/bin/python
#coding=utf-8

import sys
import os

reload(sys)
sys.setdefaultencoding('utf8')

from scrapy.selector import Selector
from scrapy.http import Request
# from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request, HtmlResponse
# from scrapy.utils.response import get_base_url
# import urlparse
import time
# import re
from spider.tools.common import *
from spider.tools.db import DB
from spider.tools.redisdb import redisDB
from spider.tools.match.parser import *
from spider.tools.download import *

class DmozSpider(CrawlSpider):
    name = 'dmoz'
    new_name = ''
    xml = None
    allowed_domains = []
    start_urls = []
    website_url = ''
    # 对应站点编号
    website_id = 0
    rules = ()
    # 数据库
    db = None
    # 爬虫起始时间
    start_time = None
    # 是否读取数据库中链接
    is_read_db_urls = False

    # 匹配模式
    xpath_str = 'sg_parser'

    xpath_object = None
    # 匹配Item
    xpath_item = 'SgGoodsItem'

    link_db = 'sg'

    first_time = True

    def __init__(self, n=None,r=None, *a, **kw):
        self.first_time = True
        # 爬虫起始时间
        self.start_time = int(time.time())
        if n == None:
            logs(time.strftime("------%Y-%d-%d %H:%M:%S ") +' Spider Name No Exits.')
            exit(0)

        new_name = sys.argv[3].replace('n=','')
        infile = os.getcwd()+r'/spider/website/' + new_name
        if os.path.exists(infile):
            logs(time.strftime("======%Y-%m-%d %H:%M:%S Spider") +' ' + new_name + ' Start Read.')
            self.xml = Selector(text=file(infile,"a+").read(), type='xml')
        else:
            logs(time.strftime("------%Y-%d-%d %H:%M:%S ") +' ' + new_name +' No Exits.')
            exit(0)

        new_name = new_name.replace('.xml','')
        self.name = self.name +':'+ new_name
        self.new_name = new_name

        link_db = self.xml.xpath("//site/@link_db").extract()
        if link_db:
            self.link_db = link_db[0].strip()
        self.db = DB(self.link_db)
        # 是否启用
        enable = self.xml.xpath("//site/@enable").extract()[0].strip()
        if enable != '1':
            if r == None:
                logs(time.strftime("------%Y-%d-%d %H:%M:%S ") +' ' + new_name +' No Enable.')
                exit(0)

        # 设置匹配模式
        xpath = self.xml.xpath("//site/@xpath").extract()
        if xpath:
            self.xpath_str = xpath[0].strip()
        try:
            # print self.xpath_str
            self.xpath_object = eval(self.xpath_str+'(self.link_db)')
        except:
            logs(time.strftime("------%Y-%d-%d %H:%M:%S ") +' xpath model not found.')
            exit(0)

        # 设置运行域名
        self.website_url = self.xml.xpath("//site/@url").extract()[0].strip()
        self.allowed_domains.append(self.website_url)

        domains = self.xml.xpath("//allowed_domains/url/@url").extract()
        if domains:
            for domain in domains:
                self.allowed_domains.append( domain.strip())

        self.website_id = self.xml.xpath("//site/@website_id").extract()[0].strip()
        is_read_url = self.xml.xpath("//site/@is_read_url").extract()[0].strip()

        if is_read_url:
            self.is_read_db_urls = True

        # 设置起始URL
        start_url = self.xml.xpath("//site/startUrls/url")
        if start_url:
            for url in start_url:
                #start_url_xpath = Selector(text=url, type='xml')
                link = url.xpath('@url').extract()
                link_page = url.xpath('@page').extract()
                if link:
                    page_url =link[0].strip()
                    self.start_urls.append(page_url)

                    # 设置多页
                    if link_page:
                        int_page = link_page[0]
                        if int_page :
                            for i in range(2, int(int_page)):
                                self.start_urls.append(re.sub(re.compile('page=\d+'), 'page='+str(i),page_url))
        # 设置链接规则
        url_rule = self.xml.xpath("//site/queueRules/rule")
        rules = []
        for rule in url_rule:
            str_allow = rule.xpath("@rule").extract()
            str_allow = '' if len(str_allow)<1 else str_allow[0].strip()
            str_deny = rule.xpath("@deny").extract()
            str_deny = '' if len(str_deny)<1 else str_deny[0].strip()
            str_callback = rule.xpath("@callback").extract()
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


        #是否清空redis
        if r == None:
            # 初始化redis
            redis = redisDB()
            redis.flushSpider(new_name)

        # 执行初始化
        super(DmozSpider, self).__init__(*a, **kw)
        self._compile_rules()

    # 设置配置区域
    def set_crawler(self, crawler):
        super(DmozSpider, self).set_crawler(crawler)
        IMAGES_STORES = crawler.settings.get('IMAGES_STORE')+'/'+self.link_db
        crawler.settings.set('IMAGES_STORE', IMAGES_STORES)

    #################每次初始化读取现有链接#################
    def _requests_to_follow(self, response):
        if not isinstance(response, HtmlResponse):
            return
        self.is_read_db_urls = False
        # 第一次把已经抓取的商品重新读取出来
        if self.is_read_db_urls:
            links = self.xpath_object.get_all_url(self.website_id)
            for n, rule in enumerate(self._rules):
                for link in links:
                    r = Request(url=link['url'], callback='parse_item')
                    r.meta.update(rule=n, link_text='old page')
                    yield rule.process_request(r)
            self.is_read_db_urls = False

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

    def parse(self, response):
        print response.url
        print '--------------------------'
        if self.new_name == 'grouponmy':
            return  self.parse_links(response)

        if self.xpath_str == 'my_ensogo' or self.xpath_str == 'xml_parser':
            return self.xpath_object.run(spider=self, response=response, xml=self.xml)
        else:
            return self._parse_response(response, self.parse_start_url, cb_kwargs={}, follow=True)

    # add links
    def parse_links(self,response):
        if self.first_time:
            self.first_time = False
            links_list = self.xml.xpath("//seedsUrls/url/@url").extract()
            dw = BrowserBase()
            for link in links_list:
                print link
                print '====================='
                html = dw.read(link)
                #print html
                hsx = Selector(text=html,type='xml')
                links = hsx.xpath("//item/link/text()").extract()
                #print links
                if links:
                    i = 0
                    for url in links:
                        i = i+1
                        # if i > 200:
                        #     break
                        print url
                        print '-----------------------'
                        rs = re.match(r'(http://www.groupon.my/deals/.*)\?.*$', url)
                        #print rs.groups()[0]
                        if rs:
                            yield Request(rs.groups()[0], callback=self.parse_item)

    # 选择匹配模式
    def parse_item(self, response):
        return self.xpath_object.run(spider=self, response=response, xml=self.xml)

    u''' 爬虫结束时操作 会反馈真实停止状态 '''
    def closed(self,reason):
        ''' 自然完成后更新隐藏信息 '''
        logs(time.strftime("======%Y-%m-%d %H:%M:%S Spider ")  +' '+ self.name + ' Stop.')
        if reason == 'finished':

            u'隐藏过期商品'
            # self.db.execute("UPDATE le_goods SET isshow=0 WHERE uptime<%s AND website_id=%s AND isshow=1", [self.start_time, self.website_id])
            # u'显示没过期商品'
            # self.db.execute("UPDATE le_goods SET isshow=1 WHERE uptime>%s AND website_id=%s AND isshow=0", [self.start_time, self.website_id])
            #self.db.close()
            pass
