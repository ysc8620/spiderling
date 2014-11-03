# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#from datetime import datetime
import MySQLdb
from  datetime import *
import hashlib
from pymongo import Connection
import common
#from scrapy import log
'''
商品结构
_id,  unique_id(唯一编号 md5(website + website_goods_id )), title, price, original_price, img,
img_list( 数组 多图片), brand, category, category_list(数组 分类组合)
description, from_url, from_website(来自网站), status(1默认显示， 2 隐藏，), add_time, update_time
'''
try:
    #conn=MySQLdb.connect(host='localhost',user='root',passwd='LEsc2008',db='winelo',port=3306,charset='utf8')
    conn=MySQLdb.connect(host='localhost',user='root',passwd='24abcdef',db='winelo',port=3306,charset='utf8',unix_socket='/tmp/mysql.sock')
    #cur=conn.cursor()
    cur = conn . cursor ( cursorclass = MySQLdb . cursors . DictCursor )# 按字段返回结果集
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

con = Connection('localhost', 27017)
db = con.test
table = db.goods

# 查找所有需要更新对象
datalist = table.find({"status":"1"})

dt = datetime.now()
for row in datalist:
    # 操作更新
    #table.update({"unique_id":row["unique_id"]},{"$set":{"status":"0"}})

    cur.execute('SELECT * FROM wl_items WHERE unique_id="'+row['unique_id']+'"')
    info = cur.fetchone()

    if info == None:
        # into item table
        # user_id,shop_id,item_title,item_title_url,item_description,price,quantity,category_id,general_category,ship_from_country,status(things),created_on,modified_on,item_color,fav_count,comment_count,bm_redircturl
        if row['title'] == '':
            print row['unique_id']
            continue
        #info = cur.exec
        data = {}
        data['user_id'] = '4'
        data['shop_id'] = '4'
        data['item_title'] = row['title']
        data['item_title_url'] = common.get_seo_title(row['title'])
        data['item_description'] = row['description']
        data['price'] = row['price']
        data['quantity'] = '0'
        data['category_id'] = '4'
        data['general_category'] = row['category']
        data['ship_from_country'] ='0'
        data['status'] = 'things'
        data['created_on'] = dt.strftime('%Y-%m-%d %H:%M:%S')
        data['modified_on'] = dt.strftime('%Y-%m-%d %H:%M:%S')
        data['fav_count'] = '0'
        data['comment_count'] = '0'
        data['bm_redircturl'] = row['from_url']
        data['website'] = row['from_website']
        data['unique_id'] = row['unique_id']
        data['collection_id'] = '0'
        data['collection_name'] = ''
        data['item_color'] = ''
        data['report_flag'] = ''
        data['ship_from_country'] = '0'
        #print data
        try:
            cur.execute('INSERT INTO wl_items(user_id,shop_id,item_title,item_title_url,item_description,price,'+
                'quantity,category_id,general_category,status,created_on,modified_on,fav_count,'+
                'comment_count,bm_redircturl,website,unique_id,collection_id,collection_name,item_color,report_flag,ship_from_country)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                (data['user_id'],data['shop_id'],data['item_title'],data['item_title_url'],data['item_description'],
                 data['price'],data['quantity'],data['category_id'],data['general_category'],data['status'],
                 data['created_on'],data['modified_on'],data['fav_count'],data['comment_count'],data['bm_redircturl'],
                 data['website'],data['unique_id'],data['collection_id'],data['collection_name'],data['item_color'],data['report_flag'],data['ship_from_country']))
            #
            id = conn.insert_id()
            if row['img_list']:
                for img in row['img_list']:
                    image_guid = hashlib.sha1(img).hexdigest()
                    path = image_guid[0:2]
                    data = {}
                    data['item_id'] = id
                    data['image_name'] = path+'/'+image_guid+'.jpg'
                    data['created_on'] = dt.strftime('%Y-%m-%d %H:%M:%S')
                    cur.execute("INSERT INTO wl_photos(item_id, image_name, created_on)VALUES(%s,%s,%s)",(data['item_id'],data['image_name'],data['created_on']))
            elif row['img']:
                image_guid = hashlib.sha1(row['img']).hexdigest()
                path = image_guid[0:2] #thumbs
                data = {}
                data['item_id'] = id
                data['image_name'] = path+'/'+image_guid+'.jpg'
                data['created_on'] = dt.strftime('%Y-%m-%d %H:%M:%S')
                cur.execute("INSERT INTO wl_photos(item_id, image_name, created_on)VALUES(%s,%s,%s)",(data['item_id'],data['image_name'],data['created_on']))
        except Exception, e:
            print e
            continue
    # 更新操作
    else:
        data = {}
        data['item_title'] = row['title']
        data['item_title_url'] = common.get_seo_title(row['title'])
        data['item_description'] = row['description']
        data['price'] = row['price']
        data['general_category'] = row['category']
        data['modified_on'] = dt.strftime('%Y-%m-%d %H:%M:%S')
        data['bm_redircturl'] = row['from_url']
        table.update({'unique_id':info["unique_id"]}, {'$set':data})

# 总提交入库
try:
    conn.commit()
except:
    pass
# 释放Mongodb资源
try:
    con.close()
except:
    pass

# 释放mysql资源
try:
    cur.close()
    conn.close()
except:
    pass
