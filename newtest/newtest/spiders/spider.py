# -*- coding: utf-8 -*-
__author__ = 'ShengYue'
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from newtest.items import TorrentItem

class MininovaSpider(CrawlSpider):
    name = 'dmoz'
    allowed_domains = ['news.cnblogs.com']
    start_urls = ['http://news.cnblogs.com/']
    rules = [
        Rule(LinkExtractor(allow=[r'^http://news.cnblogs.com/n/page/\d+/$'])),
        Rule(LinkExtractor(allow=[r'^http://news.cnblogs.com/n/\d+/$']), 'parse_torrent')
    ]

    def parse_torrent(self, response):
        torrent = TorrentItem()
        torrent['url'] = response.url
        torrent['name'] = response.xpath("//title/text()").extract()[0]
        #open('system.log', 'ab').write(response.url)
        #open('system.log', 'a+').write(response.xpath("//title/text()").extract()[0])
        return torrent