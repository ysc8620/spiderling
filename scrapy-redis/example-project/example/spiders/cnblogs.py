# -*- coding: utf-8 -*-
__author__ = 'ShengYue'
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from example.items import ExampleItem
from scrapy.selector import Selector

class MininovaSpider(CrawlSpider):
    name = "cnblogxx"
    allowed_domains = ["news.cnblogs.com"]
    start_urls = [
        "http://news.cnblogs.com/",
    ]
    rules = (
        #下面是符合规则的网址,但是不抓取内容,只是提取该页的链接(这里网址是虚构的,实际使用时请替换)
        Rule(LinkExtractor(allow=(r'http://news.cnblogs.com/n/page/\d+/'))),
        #Rule(LinkExtractor(allow=(r'http://news.cnblogs.com/n/\d+/'))),
        Rule(LinkExtractor(allow=(r'http://news.cnblogs.com/'))),
        #下面是符合规则的网址,提取内容,(这里网址是虚构的,实际使用时请替换)
        Rule(LinkExtractor(allow=(r'http://news.cnblogs.com/n/\d+/')), 'parse_item'),
    )

    def parse(self, response):
        open('cn.log','a+').write('1.' + response.url+'\r\n')
        el = ExampleItem()
        el['name'] ='a/text()'
        el['description']= 'text()'
        el['link']= 'a/@href'
        el['url']= response.url
        yield el

    def parse_item(self, response):
        open('cn.log','a+').write('2.' + response.url+'\r\n')
        el = ExampleItem()
        el['name'] = response.url
        el['description']= 'text()'
        el['link']= response.url
        el['url']= response.url
        yield el

        #`id`, `original_id`, `name`, img, `brand`, `price`, `original_price`, `weight`, `description`, `from_url`, `website_id`, `update_time`, `addtime`
        # sel = Selector(response)
        # torrent = TorrentItem()
        # name = sel.xpath('//div[@class="prod"]/h1/text()').extract()
        # torrent['name'] = '' if len(name)<1 else name[0].strip()
        # torrent['original_id'] = '0'
        # brand = sel.xpath('//div[@class="prod"]/h2/text()').extract()
        # torrent['brand'] = '' if len(brand)<1 else brand[0].strip()
        # price = sel.xpath('//div[@class="prod"]/p[@class="big-price"]/text()').re(r'\s*¥(\w+)\s*')
        # torrent['price'] = '' if len(price)<1 else price[0]
        # src = sel.xpath('//div[@class="img_container"]/img/@src').extract()
        # torrent['img'] = '' if len(src)<1 else src[0].strip()
        # torrent['original_price'] = '0'
        # desc = sel.xpath('//div[contains(@class,"prod_content")]').extract()
        # torrent['description'] = '' if len(desc)<1 else desc[0].strip()
        # torrent['website_id'] = '0'
        # torrent['from_url'] = response.url
        # return torrent