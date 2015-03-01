#!/usr/bin/python
#coding=utf-8

import sys,os
reload(sys)
sys.setdefaultencoding('utf8')
import redis


class redisDB:
    conn = None
    r = None
    def connect(self):
        if self.conn:
            pass
        else:
            try:
                self.conn = redis.StrictRedis(host='127.0.0.1', port=6379)
            except:
                print 'Redis Connect error.'

    u'清空指定爬虫数据'
    def flushSpider(self, spider):
        self.connect()
        print self.conn.delete('dmoz:'+spider+':requests')
        print self.conn.delete('dmoz:'+spider+':dupefilter')
        print self.conn.delete('dmoz:'+spider+':items')

    u'清空所有数据'
    def flushAll(self):
        print self.conn.flushall()

    def close(self):
        pass


# s = redisDB()
# s.flushSpider('imobshop')