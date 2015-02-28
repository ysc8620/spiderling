#!/usr/bin/python
#coding=utf-8

import sys,os
reload(sys)
sys.setdefaultencoding('utf8')

from scrapy.selector import Selector
# from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from spider.items import DealItem
from scrapy.utils.response import get_base_url
import urlparse
import time
import re
from spider.tools.common import *
from spider.tools.db import DB

class DmozSpider(CrawlSpider):
    name = 'dmoz'
    xml = None
    allowed_domains = []
    start_urls = []
    website_url = ''
    rules = ()
    db = None
    def __init__(self, *a, **kw):
        new_name = ''
        if len(sys.argv) > 3:
            new_name = sys.argv[3].replace('name=','')
        infile = os.getcwd()+r'/spider/spiders/website/' + new_name
        if os.path.exists(infile):
            logs(time.strftime("======%Y-%d-%d") + new_name + ' Start Read.')
            str = file(infile,"a+").read()
            self.xml = Selector(text=str, type='xml')
        else:
            logs(time.strftime("%Y-%d-%d") + new_name +' No Exits.')

        self.name = self.name +':'+ new_name.replace('.xml','')
        # 设置运行域名
        self.allowed_domains.append(self.xml.xpath("//site/@url").extract()[0].strip())
        self.website_url = self.xml.xpath("//site/@url").extract()[0].strip()
        self.db = DB()
        # 起始URL
        start_url = self.xml.xpath("//site/startUrls/url/@url").extract()
        if start_url:
            for url in start_url:
                self.start_urls.append(url.strip())
        # 链接规则
        url_rule = self.xml.xpath("//site/queueRules/rule").extract()
        rules = []
        for str in url_rule:
            sl = Selector(text=str, type='xml')
            allow = sl.xpath("//rule/@rule").extract()
            allow = '' if len(allow)<1 else allow[0].strip()
            deny = sl.xpath("//rule/@deny").extract()
            deny = '' if len(deny)<1 else deny[0].strip()
            calls = sl.xpath("//rule/@callback").extract()
            calls = '' if len(calls)<1 else calls[0].strip()

            if calls != '':
                ru = Rule(LinkExtractor(allow=r""+allow),callback=calls)
            else:
                ru = Rule(LinkExtractor(allow=r""+allow))
            rules.append(ru)
        self.rules = tuple(rules)
        super(DmozSpider, self).__init__(*a, **kw)
        self._compile_rules()

    def parse_item(self, response):
        hs = Selector(response)
        base_url = get_base_url(response)
        imgs = []

        item = DealItem()
        for name,value in vars(DealItem).items():
            if name=='fields':
                for i in value:
                    item[i] = ''
                #print('%s=%s'%(name,value))
        item['image_urls'] = item['img_urls'] = imgs

        url_id = hs.xpath('//input[@name="product"]/@value').extract()
        if url_id:
            id = url_id[0].strip()
            #item['name'] = hashlib.sha1(id).hexdigest()
        else:
            item['name'] = False
            return item

        title = hs.xpath('//div[@class="product-name"]/h1/text()').extract()
        item['name'] = '' if len(title)<1 else title[0].strip()

        price = hs.xpath('//p[@class="special-price"]//span[@class="price"]/text()').extract()
        item['price'] = '' if len(price)<1 else price[0].strip().replace('S$','').strip()

        original_price = hs.xpath('//p[@class="old-price"]//span[@class="price"]/text()').extract()
        item['originalPrice'] = '' if len(original_price)<1 else original_price[0].strip().replace('S$','').strip()

        img_list = hs.xpath('//div[contains(@class,"default-views")]//li/a/@href').extract()

        for i in img_list:
            imgs.append(urlparse.urljoin(base_url, i.strip()))

        item['url'] = response.url
        item['countBought'] = 0
        item['website_id'] = 76
        item['ExpiryTime'] = int(time.time()) + 2592000

        description = hs.xpath('//div[@id="product_tabs_description_contents"]').extract()
        description = '' if len(description)<1 else description[0].strip()
        if description:
            description = re.subn(r"\s+"," ",description)[0]
            item['description'] = description
            #description = re.subn(r'<(div).*?>([\s\S]*?)<\/(div)>',r"\2",description)[0]

        # cate
        category = hs.xpath('//div[@class="breadcrumbs"]//li[contains(@class,"category")]/a/text()').extract()
        item['cate'] = '' if len(category)<1 else category[len(category)-1].strip()

        item['highlight'] = ''
        item['condition'] = ''
        #product-attribute-specs-table
        address = hs.xpath('//div[@id="product_tabs_additional_contents"]//th[contains(.//text(), "Seller Address")]/ancestor::tr/td/text()').extract()
        address = '' if len(address)<1 else address[0].strip()
        item['address'] = address

        postCode = hs.xpath('//div[@id="product_tabs_additional_contents"]//th[contains(.//text(), "Seller Postal Code")]/ancestor::tr/td/text()').extract()
        postCode = '' if len(postCode)<1 else postCode[0].strip()
        item['postCode'] = postCode

        merchant = hs.xpath('//div[@id="product_tabs_additional_contents"]//th[contains(.//text(), "Seller Name")]/ancestor::tr/td/text()').extract()
        merchant = '' if len(merchant)<1 else merchant[0].strip()
        item['merchant'] = merchant

        phone = hs.xpath('//div[@id="product_tabs_additional_contents"]//th[contains(.//text(), "Seller Phone")]/ancestor::tr/td/text()').extract()
        phone = '' if len(phone)<1 else phone[0].strip()
        item['phone'] = phone

        item['oldImg'] = imgs
        item['descOldImg'] = imgs
        if len(imgs) > 0 :
            item['image_urls'] = imgs
        return item
    def closed(self,reason):
        # print ===finished+++++
        ''' 自然完成后更新隐藏信息 '''
        if reason == 'finished':
            pass

