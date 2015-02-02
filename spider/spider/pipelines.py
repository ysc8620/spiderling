# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime
import time
import string
#import MySQLdb
#import hashlib
import json
from tools.common import *
from pymongo import Connection

'''
商品结构
_id,  unique_id(唯一编号 md5(website + website_goods_id )), title, price, original_price, img,
img_list( 数组 多图片), brand, category, category_list(数组 分类组合)
description, from_url, from_website(来自网站), status(1默认显示， 2 隐藏，), add_time, update_time
'''
class GoodsPipeline(object):
    def __init__(self):
        #self.connection = MySQLdb.connect(user = 'root',db='test',passwd = 'LEsc2008',host='localhost')#,unix_socket='/tmp/mysql.sock'
        pass
        # self.con = Connection('localhost', 27017)
        # self.db = self.con.test
        # self.table = self.db.goods


    '''
    name,url,oldImg,descOldImg,cate,price,originalPrice,countBought,ExpiryTime,
    highlight,condition,description,address,postCode,merchant,phone

    `last_modified`, `goods_id`, `uid`, `img`, `deal_img`, `display_order`, `img_w`, `img_h`,
    `desc_bigpic`, `bigpic`, `small_pic`, `desc_oldimg`, `oldimg`, `name`, `seo_title`, `url`,
    `currency`, `original_price`, `price`, `cate_id`, `source`, `addtime`, `expiry_time`, `uptime`,
    `website_id`, `store_id`, `isdeal`, `ispublish`,isshow`,`highlight`, `conditions`, `description`,
    `merchant`, `phone`, `address`, `city`, `country`, `post`
    '''
    def process_item(self, item, spider):
        sql = "INSERT INTO le_goods SET `last_modified`='%s',`uid`='%s',`img`='%s', `deal_img`='%s'," \
      "`display_order`='%s',`desc_bigpic`='%s', `bigpic`='%s', `small_pic`='%s',`desc_oldimg`='%s', " \
      "`oldimg`='%s', `name`='%s', `seo_title`='%s', `url`='%s', `currency`='%s', " \
      "`original_price`='%s', `price`='%s', `cate_id`='%s', `source`='%s', `addtime`='%s'," \
      "`expiry_time`='%s', `uptime`='%s', `website_id`='%s',`isdeal`='%s',`ispublish`='%s'," \
      "isshow`='%s',`highlight`='%s', `conditions`='%s', `description`='%s', `merchant`='%s', " \
      "`phone`='%s', `address`='%s',`city`='%s', `country`='%s', `post`='%s'" % \
        (time.time(),1, item['oldImg'][0],item['oldImg'][0],
         0,''.join(item['descOldImg']),''.join(item['oldImg']),''.join(item['oldImg']),''.join(item['oldImg']),
        ''.join(item['descOldImg']),item['name'],get_seo_title(item['name']),item['url'],'SGD',
        item['price'],item['originalPrice'], 0,'reptile',time.time(),
        item['ExpiryTime'],time.time(),0,1,1,
        0,item['highlight'],item['condition'],item['description'],item['merchant'],
        item['phone'],item['address'], 1,1,item['postCode'])
        open('sql.log', 'w+').write(sql+"\r\n")

        # info = self.table.find({'unique_id':item['unique_id']})
        # if info.count() < 1:
        #     data = {}
        #     data['title'] = item['title']
        #     data['unique_id'] = str(item['unique_id'])
        #     data['price'] = item['price']
        #     data['original_price'] = item['original_price']
        #     data['img'] = item['img']
        #     data['img_list'] = item['img_list']
        #     data['brand'] = item['brand']
        #     data['category'] = item['category']
        #     data['category_list'] = item['category_list']
        #     data['description'] = item['description']
        #     data['from_url'] = item['from_url']
        #     data['from_website'] = item['from_website']
        #     data['status'] = str(item['status'])
        #     data['add_time'] = str(item['add_time'])
        #     data['update_time'] = str(item['update_time'])
        #
        #     self.table.insert(data)


        #cursor = self.connection.cursor()
        #cursor.execute('insert into links(url,md5url)values(%s, %s)', (item['from_url'],hashlib.md5(item['from_url']).hexdigest()))
        return item