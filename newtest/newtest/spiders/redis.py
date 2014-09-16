# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider

class Redis(RedisSpider):
    name = 'redis'
    start_urls = ['http://news.cnblogs.com/']
    redis_key = 'myspider:start_urls'

    def parse(self, response):
        open('log.log', 'a+').write(response.url)
        # do stuff
        pass