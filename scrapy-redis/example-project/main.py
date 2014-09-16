#import redis
import MySQLdb
#import scrapy.contrib.pipeline.images.ImagesPipeline

# pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
# r = redis.Redis(connection_pool=pool)
#
# #r.set('name', 'hello')
# print r.llen('dmoz:items')

conn = MySQLdb.connect(user = 'root',db='test',passwd = '24abcdef',host='127.0.0.1')
cursor = conn.cursor()
cursor.execute('insert into links(url,md5url)values(%s, %s)', ('url','url'))
