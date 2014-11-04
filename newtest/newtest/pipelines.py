# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

# class NewtestPipeline(object):
#     def process_item(self, item, spider):
#         return item

#from twisted.enterprise import adbapi
import time
from scrapy import log
import MySQLdb.cursors

class SQLStorePipeline(object):
    def __init__(self):
        self.connection = MySQLdb.connect(user = 'root',db='test',passwd = 'LEsc2008',host='localhost',charset="utf8")
        #self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        # create record if doesn't exist.
        # all this block run on it's own thread
        #print "insert into goods (title, img, url, add_time) values (%s, %s,%s, %s)"
        #s = self.cursor.execute("select * from goods where title = %s", (item['name'], ))
        #print item["name"]
        cursor = self.connection.cursor()
        cursor.execute("insert into goods (title, img, url, add_time) values (%s, %s,%s, %s)",(item['name'],item['img'],item['from_url'],time.time()))
        return item

