# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider

from urlparse import urljoin

from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from spiderling.items import SpiderlingItem
from spiderling.pipelines import SpiderlingPipeline
import re


class DmozSpider(CrawlSpider):
    name = "dmoz"
    allowed_domains = ["news.cnblogs.com"]
    start_urls = [
        "http://news.cnblogs.com/",
    ]
    rules = (
        #下面是符合规则的网址,但是不抓取内容,只是提取该页的链接(这里网址是虚构的,实际使用时请替换)
        Rule(SgmlLinkExtractor(allow=(r'http://news.cnblogs.com/n/page/\d+/'))),
        Rule(SgmlLinkExtractor(allow=(r'http://news.cnblogs.com/n/\d+/'))),
        Rule(SgmlLinkExtractor(allow=(r'http://news.cnblogs.com/'))),
        #下面是符合规则的网址,提取内容,(这里网址是虚构的,实际使用时请替换)
        Rule(SgmlLinkExtractor(allow=(r'http://news.cnblogs.com/n/\d+/')), callback='parse_item'),
    )

    def parkse(self, response):
        #exit('---------')
        #print 'hello'
        items = []
        item = SpiderlingItem()
        item['name'] = 'hello'
        items.append(item)
        return response
        #open('system.log', 'wb').write(response.url)
        # items = []
        # hxs = HtmlXPathSelector(response)
        # #print hxs.select('//title/text()').extract()[0]
        # item = DmozItem()
        # item['title'] =  hxs.select('//title/text()').extract()[0]
        #
        # item['link'] =  hxs.select('//title/text()').extract()[0]
        # item['desc'] =  hxs.select('//title/text()').extract()[0]
        #
        # items.append(item)
        # return items

    def parse_item(self, response):
        exit('--')
        print response.url
        print response.url
        print response.url
        print response.url
        print response.url
        items = []
        item = SpiderlingItem()
        item['name'] = 'ss'
        items.append(item)
        return items