#coding=utf-8
__author__ = 'Administrator'
import json
import time, re,os
from scrapy.selector import Selector
from scrapy.http import Request
# from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request, HtmlResponse

from scrapy.selector import Selector
new_name = 'ensogo.com.my.xml'
strs = file(os.getcwd()+r'/spider/website/' + new_name,"a+").read()

xml = Selector(text=strs, type='xml')
start_url = xml.xpath("//site/startUrls/url").extract()
for url in start_url:
    start_url_xpath = Selector(text=url, type='xml')
    url = start_url_xpath.xpath('//@url').extract()
    page = start_url_xpath.xpath('//@page').extract()
    if url:
        print url[0]
        if page:
            page_ii = int(page[0])
            for i in range(2, page_ii):
                print re.sub(re.compile('page=\d+'), 'page='+str(i),url[0])
                #print url[0].sub('page=\d+', 'page='+str(i))
