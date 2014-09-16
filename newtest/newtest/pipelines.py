# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

# class NewtestPipeline(object):
#     def process_item(self, item, spider):
#         return item

from twisted.enterprise import adbapi
import datetime
from scrapy import log
import MySQLdb.cursors

class SQLStorePipeline(object):

    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb', db='test',
                user='root', passwd='LEsc2008', cursorclass=MySQLdb.cursors.DictCursor,
                charset='utf8', use_unicode=True)

    def process_item(self, item, spider):
        # run db query in thread pool
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)

        return item

    def _conditional_insert(self, tx, item):
        # create record if doesn't exist.
        # all this block run on it's own thread
        tx.execute("select * from goods where name = %s", (item['name'], ))
        result = tx.fetchone()
        if result:
            log.msg("Item already stored in db: %s" % item, level=log.DEBUG)
        else:
            #`id`, `original_id`, `name`, `brand`, `price`, `original_price`, `weight`, `description`, `from_url`, `website_id`, `update_time`, `addtime`

            tx.execute(\
                "insert into goods (original_id, name, img, brand,  price, original_price, description, from_url, website_id, update_time, addtime) "
                "values (%s, %s,%s, %s, %s,%s, %s, %s, %s,%s, %s)",
                (item['original_id'],
                 item['name'],
                 item['img'],
                 item['brand'],
                 item['price'],
                 item['original_price'],
                 item['description'],
                 item['from_url'],
                 item['website_id'],
                 datetime.datetime.now(),
                 datetime.datetime.now())
            )
            log.msg("Item stored in db: %s" % item, level=log.DEBUG)

    def handle_error(self, e):
        log.err(e)