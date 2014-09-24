#-*-coding:utf-8-*-
__author__ = 'ShengYue'

from pymongo import Connection
from pyes import *

# conn = ES('127.0.0.1:9200')
# try:
#     conn.indices.delete_index("goods-index")
# except:
#      pass
# conn.indices.create_index('goods-index') #
# mapping = {
#             u'name':{'boost': 1.0,'index': 'analyzed','store': 'yes','type': u'string',"term_vector" : "with_positions_offsets"},
#             #u'brand':{'boost': 1.0,'index': 'not_analyzed','store': 'yes','type': u'string'},
#             #u'category':{'boost': 1.0,'index': 'not_analyzed','store': 'yes','type': u'string'},
#             #u'price':{'boost': 1.0,'index': 'not_analyzed','store': 'yes','type': u'string'},
#             #u'add_time':{'boost': 1.0,'index': 'not_analyzed','store': 'yes','type': u'string'},
#             u'unique_id':{'boost': 1.0,'index': 'not_analyzed','store': 'yes','type': u'string'}
#           }
# conn.indices.put_mapping("goods", {'properties':mapping}, ["goods-index"])
# con = Connection('localhost', 27017)
# db = con.test
# goods_list = db.goods.find()
# i = 1
# for goods in goods_list:
#     conn.index({'name':goods['title'],'unique_id':goods['unique_id']}, 'goods-index', 'goods', i, True)
#     i = i + 1
#                  #向human的man中添加索引
# conn.indices.refresh()
#
# con.close()

conn = ES('127.0.0.1:9200') # Use HTTP

try:
    conn.indices.delete_index("test-index")
except:
    pass

conn.indices.create_index("test-index")

mapping = {
    'parsedtext': {
        'boost': 1.0,
        'index': 'analyzed',
        'store': 'yes',
        'type': 'string',
        "term_vector": "with_positions_offsets"
    },
    'name': {
        'boost': 1.0,
        'index': 'analyzed',
        'store': 'yes',
        'type': 'string',
        "term_vector": "with_positions_offsets"
    },
    'title': {
        'boost': 1.0,
        'index': 'analyzed',
        'store': 'yes',
        'type': 'string',
        "term_vector": "with_positions_offsets"
    },
    'pos': {
        'store': 'yes',
        'type': 'integer'
    },
    'uuid': {
        'boost': 1.0,
        'index': 'not_analyzed',
        'store': 'yes',
        'type': 'string'
    }
}
conn.indices.put_mapping("test-type", {'properties':mapping}, ["test-index"])


conn.index({"name":"Joe Tester", "title":"sssss", "parsedtext":"Joe Testere nice guy", "uuid":"11111", "position":1}, "test-index", "test-type", 'sdfsdfsdfsdfs')
conn.index({"name":"Bill Baloney",  "title":"ssssdddss","parsedtext":"Joe Testere nice guy", "uuid":"22222", "position":2}, "test-index", "test-type",'sdfsdfsdfsfsfewrwsddfsdfs')


conn.indices.refresh("test-index") # Single index.
#conn.indices.refresh(["test-index", "test-index-2"]) # Multiple Indexes

q = TermQuery("name", "joe")
results = conn.search(query = q)
for r in results:
   print r




