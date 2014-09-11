# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SpiderlingPipeline(object):
    def process_item(self, item, spider):
        return item

    def parse_item(self, item,spider):
        print 'ok'
        #print item
        return item

    def parse(self, item,spider):
        print 'ok'
        #print item
        return item
