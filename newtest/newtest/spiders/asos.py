# -*- coding: utf-8 -*-
__author__ = 'ShengYue'
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from newtest.items import TorrentItem
from scrapy.selector import Selector

class MininovaSpider(CrawlSpider):
    name = 'asos'
    allowed_domains = ['asos.cn']
    start_urls = ['http://www.asos.cn/']
    rules = [
        Rule(LinkExtractor(allow=[r'^http://www.asos.cn/c/\S+'])),
        Rule(LinkExtractor(allow=[r'^http://www.asos.cn/p/\S+']),  'parse_torrent')
    ]

    def parse_torrent(self, response):
        #`id`, `original_id`, `name`, img, `brand`, `price`, `original_price`, `weight`, `description`, `from_url`, `website_id`, `update_time`, `addtime`
        sel = Selector(response)
        torrent = TorrentItem()
        name = sel.xpath('//div[@class="prod"]/h1/text()').extract()
        torrent['name'] = '' if len(name)<1 else name[0].strip()
        torrent['original_id'] = '0'
        brand = sel.xpath('//div[@class="prod"]/h2/text()').extract()
        torrent['brand'] = '' if len(brand)<1 else brand[0].strip()
        price = sel.xpath('//div[@class="prod"]/p[@class="big-price"]/text()').re(r'\s*¥(\w+)\s*')
        torrent['price'] = '' if len(price)<1 else price[0]
        src = sel.xpath('//div[@class="img_container"]/img/@src').extract()
        torrent['img'] = '' if len(src)<1 else src[0].strip()
        torrent['original_price'] = '0'
        desc = sel.xpath('//div[contains(@class,"prod_content")]').extract()
        torrent['description'] = '' if len(desc)<1 else desc[0].strip()
        torrent['website_id'] = '0'
        torrent['from_url'] = response.url
        return torrent