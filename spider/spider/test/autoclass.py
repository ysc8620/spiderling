#!/usr/bin/python
#coding=utf-8
import time
import sys,os,json

sys.path.append( '/wwwroot/spiderling/spider')
from spider.tools.db import *
from spider.tools.SimpleClassifier import *

reload(sys)

db = DB('sg')
scf = SimpleClassifier('sg')

res = db.execute('SELECT goods_id, name,cate_id FROM le_goods WHERE website_id in(76,6)')
goods_list = res.fetchall()

for goods in goods_list:
    print goods['goods_id']
    #print classlist
    if goods['cate_id'] <1:
        classlist = scf.findCateAndTags(goods['name'],4)
        if classlist['cate']:
            db.execute('UPDATE le_goods SET cate_id=%s WHERE goods_id=%s',[classlist['cate'], goods['goods_id']])
            db.execute("INSERT INTO le_cate_goods_index SET cate_id=%s, goods_id=%s,weight=0",[classlist['cate'], goods['goods_id']])
            for cate_id in classlist['cates']:
                db.execute("INSERT INTO le_cate_goods_index SET cate_id=%s, goods_id=%s,weight=0",[cate_id, goods['goods_id']])


