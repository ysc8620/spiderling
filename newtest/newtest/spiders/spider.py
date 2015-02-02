# -*- coding: utf-8 -*-
__author__ = 'ShengYue'
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from newtest.items import TorrentItem
from scrapy.selector import Selector

class MininovaSpider(CrawlSpider):
    name = 'jd'
    allowed_domains = ['jd.com','list.jd.com','item.jd.com']
    start_urls = ['http://channel.jd.com/shouji.html']
    rules = [
        Rule(LinkExtractor(allow=[r'^http://list.jd.com/list.html\S*'])),
        Rule(LinkExtractor(allow=[r'^http://item.jd.com/(\d+).html']),  'parse_torrent')
    ]

    def parse_torrent(self, response):
        #`id`, `original_id`, `name`, img, `brand`, `price`, `original_price`, `weight`, `description`, `from_url`, `website_id`, `update_time`, `addtime`
        sel = Selector(response)
        torrent = TorrentItem()
        name = sel.xpath('//div[@id="name"]/h1/text()').extract()
        torrent['name'] = '' if len(name)<1 else name[0].strip()
        torrent['original_id'] = '0'
        #brand = sel.xpath('//div[@class="prod"]/h2/text()').extract()
        torrent['brand'] = ''# if len(brand)<1 else brand[0].strip()
        price = sel.xpath('//strong[@id="jd-price"]/text()')
        torrent['price'] = '0' if len(price)<1 else price[0]
        src = sel.xpath('//div[@class="jqzoom"]/img/@src').extract()
        torrent['img'] = '' if len(src)<1 else src[0].strip()
        torrent['original_price'] = '0'
        torrent['description'] = ''
        torrent['website_id'] = '0'
        torrent['from_url'] = response.url
        return torrent