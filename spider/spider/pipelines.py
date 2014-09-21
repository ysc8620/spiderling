# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime
import MySQLdb
import hashlib

class GoodsPipeline(object):
    def __init__(self):
        self.connection = MySQLdb.connect(user = 'root',db='test',passwd = 'LEsc2008',host='localhost')#,unix_socket='/tmp/mysql.sock'

    def process_item(self, item, spider):
        item["crawled"] = datetime.utcnow()
        item["spider"] = spider.name
        cursor = self.connection.cursor()
        cursor.execute('insert into links(url,md5url)values(%s, %s)', (item['url'],hashlib.md5(item['url']).hexdigest()))
        #cursor.commit()
        return item