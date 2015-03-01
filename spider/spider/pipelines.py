#!/usr/bin/python
#coding=utf-8

import sys,os
reload(sys)
sys.setdefaultencoding('utf8')

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime
import time
from tools.db import DB
import MySQLdb
#import hashlib
import json
from tools.common import *
# from pymongo import Connection
'''
商品结构
_id,  unique_id(唯一编号 md5(website + website_goods_id )), title, price, original_price, img,
img_list( 数组 多图片), brand, category, category_list(数组 分类组合)
description, from_url, from_website(来自网站), status(1默认显示， 2 隐藏，), add_time, update_time
'''
class GoodsPipeline(object):
    def __init__(self):
        # self.connection = MySQLdb.connect(user = 'root',db='emaillist',passwd = 'ntucdbs911',host='localhost',unix_socket='/tmp/mysql.sock')#,unix_socket='/tmp/mysql.sock'
        # #self.connection = MySQLdb.connect(user = 'root',db='test',passwd = 'LEsc2008',host='localhost')
        # self.cursor = self.connection.cursor()
        # self.cursor.execute('SET NAMES utf8')

        self.db = DB()
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
        if item['name'] == False:
            return item
        img = small_pic = big_pic = old_pic = ''
        if len(item['oldImg']) > 0 :
            img = get_img_path(item['oldImg'][0], 'thumb400')
            big_pic = '|'.join(item['oldImg'])
            for src in item['oldImg']:
                small_pic = small_pic + get_img_path(src, 'thumb100') + '|'
                old_pic = old_pic + get_img_path(src)+'|'
            small_pic = small_pic.strip('|')
            old_pic = old_pic.strip('|')

        if item['goods']:
            if item['goods']['price'] != item['price'] or item['goods']['original_price'] != item['originalPrice'] or item['goods']['name'] != item['name']:
                self.db.execute("UPDATE le_goods SET name=%s,price=%s,original_price=%s, uptime=%s,expiry_time=%s,site_id=%s WHERE goods_id=%s",[item['name'],item['price'],item['originalPrice'],int(time.time()),item['ExpiryTime'], item['site_id'],item['goods']['goods_id']])
            else:
                self.db.execute("UPDATE le_goods SET uptime=%s,expiry_time=%s,site_id=%s WHERE goods_id=%s",[int(time.time()),item['ExpiryTime'], item['site_id'],item['goods']['goods_id']])
        else:
            self.db.execute("INSERT INTO le_goods SET `uid`=%s,`site_id`=%s,`img`=%s, `deal_img`=%s,`display_order`=%s,`desc_bigpic`=%s, `bigpic`=%s, `small_pic`=%s,`desc_oldimg`=%s,`oldimg`=%s, `name`=%s, `seo_title`=%s, `url`=%s, `currency`=%s,`original_price`=%s, `price`=%s, `cate_id`=%s, `source`=%s, `addtime`=%s,`expiry_time`=%s, `uptime`=%s, `website_id`=%s,`isdeal`=%s,`ispublish`=%s,`isshow`=%s,`highlight`=%s, `conditions`=%s, `description`=%s, `merchant`=%s,`phone`=%s, `address`=%s,`city`=%s, `country`=%s, `post`=%s",[1,item['site_id'], img,img,0,'',old_pic,small_pic,'',big_pic,item['name'].encode('utf-8'),get_seo_title(item['name'].encode('utf-8')),item['url'],'SGD',item['originalPrice'],item['price'], 0,'reptile',time.time(),item['ExpiryTime'],time.time(),item['website_id'],1,1,1,item['highlight'],item['condition'],item['description'].encode('utf-8'),item['merchant'].encode('utf-8'),item['phone'],item['address'].encode('utf-8'),1,1,item['postCode'].encode('utf-8')])
        return item