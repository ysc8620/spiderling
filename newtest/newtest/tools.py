# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

# class NewtestPipeline(object):
#     def process_item(self, item, spider):
#         return item

from twisted.enterprise import adbapi
import time
from scrapy import log
import MySQLdb.cursors

connection = MySQLdb.connect(user = 'root',db='test',passwd = 'LEsc2008',host='localhost',charset="utf8")

cursor = connection.cursor()
cursor.execute("insert into goods (title, img, url, add_time)values(%s, %s,%s, %s)",('name','img','from_url',time.time()))
