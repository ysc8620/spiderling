#-*-coding:utf-8-*-
__author__ = 'ShengYue'

from pymongo import Connection
from pyes import *

conn = ES('127.0.0.1:9200')
try:
    conn.indices.delete_index("godos-index")
except:
     pass
conn.indices.create_index('godos-index') #
mapping = {
            u'title':{'boost': 1.0,'index': 'analyzed','store': 'yes','type': u'string',"term_vector" : "with_positions_offsets"},
            #u'brand':{'boost': 1.0,'index': 'not_analyzed','store': 'yes','type': u'string'},
            #u'category':{'boost': 1.0,'index': 'not_analyzed','store': 'yes','type': u'string'},
            #u'price':{'boost': 1.0,'index': 'not_analyzed','store': 'yes','type': u'string'},
            #u'add_time':{'boost': 1.0,'index': 'not_analyzed','store': 'yes','type': u'string'},
            u'unique_id':{'boost': 1.0,'index': 'not_analyzed','store': 'yes','type': u'string'}
          }
conn.indices.put_mapping("goods", {'properties':mapping}, ["goods-index"])
con = Connection('localhost', 27017)
db = con.test
goods_list = db.goods.find()
i = 1
for goods in goods_list:
    conn.index({'title':goods['title'],'unique_id':goods['unique_id']}, 'godos-index', 'goods', i, True)
    i = i + 1
                 #向human的man中添加索引
conn.indices.refresh()

con.close()




