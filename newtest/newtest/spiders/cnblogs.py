# -*- coding: utf-8 -*-
import scrapy


class CnblogsSpider(scrapy.Spider):
    name = "cnblogs"
    allowed_domains = ["cnblogs.com"]
    start_urls = (
        'http://www.cnblogs.com/',
    )

    def parse(self, response):
        pass
