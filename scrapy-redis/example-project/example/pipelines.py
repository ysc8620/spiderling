#-*-codeing:utf-8-*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from datetime import datetime
import MySQLdb
import hashlib

from scrapy.http import Request
class ExamplePipeline(object):
    def __init__(self):
        self.connection = MySQLdb.connect(user = 'root',db='test',passwd = 'LEsc2008',host='localhost')

    def process_item(self, item, spider):
        open('2sys.log','a+').write(item['url']+'\r\n')
        item["crawled"] = datetime.utcnow()
        item["spider"] = spider.name
        cursor = self.connection.cursor()
        cursor.execute('insert into links(url,md5url)values(%s, %s)', (item['url'],hashlib.md5(item['url']).hexdigest()))
        #cursor.commit()
        return item