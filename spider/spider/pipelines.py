#!/usr/bin/python
#coding=utf-8

import sys,os
reload(sys)
sys.setdefaultencoding('utf8')

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
from tools.db import DB
from tools.common import *
from spider.items import *

#
'''
商品结构
_id,  unique_id(唯一编号 md5(website + website_goods_id )), title, price, original_price, img,
img_list( 数组 多图片), brand, category, category_list(数组 分类组合)
description, from_url, from_website(来自网站), status(1默认显示， 2 隐藏，), add_time, update_time
'''
class SgPipeline(object):
    conn = None
    db = None
    def install(self, db='sg'):
        if self.conn == None:
            self.db = DB(db)

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
        self.install(item['db'])
        if type(item) != SgGoodsItem:
            return item

        if item['name'] == False:
            return item

        img = small_pic = big_pic = old_pic = ''
        if len(item['images']) > 0 :
            img = '/uploaded/' + item['images'][0].replace( 'original','thumb400')
            for src in item['images']:
                small_pic = small_pic +  '/uploaded/'+ src.replace('original', 'thumb100') + '|'
                big_pic = big_pic +  '/uploaded/'+ src
            small_pic = small_pic.strip('|')
            big_pic = big_pic.strip('|')

        if len(item['oldImg']) > 0:
            old_pic = '|'.join(item['oldImg'])

        for i in item:
            if type(item[i]) == unicode or type(item[i]) == str:
                item[i] = item[i].encode('utf-8')
        if item['goods']:
            if item['goods']['price'] != item['price'] or item['goods']['original_price'] != item['originalPrice'] or item['goods']['name'] != item['name']:
                self.db.execute("UPDATE le_goods SET isshow=1,name=%s,price=%s,original_price=%s, uptime=%s,expiry_time=%s,site_id=%s WHERE goods_id=%s",[item['name'],item['price'],item['originalPrice'],int(time.time()),item['ExpiryTime'], item['site_id'],item['goods']['goods_id']])
            else:
                self.db.execute("UPDATE le_goods SET isshow=1,uptime=%s,expiry_time=%s,site_id=%s WHERE goods_id=%s",[int(time.time()),item['ExpiryTime'], item['site_id'],item['goods']['goods_id']])
        else:
            self.db.execute("INSERT INTO le_goods SET `uid`=%s,`site_id`=%s,`img`=%s, `deal_img`=%s,`display_order`=%s,`desc_bigpic`=%s, `oldimg`=%s, `small_pic`=%s,`desc_oldimg`=%s,`bigpic`=%s, `name`=%s, `seo_title`=%s, `url`=%s, `currency`=%s,`original_price`=%s, `price`=%s, `cate_id`=%s, `source`=%s, `addtime`=%s,`expiry_time`=%s, `uptime`=%s, `website_id`=%s,`isdeal`=%s,`ispublish`=%s,`isshow`=%s,`highlight`=%s, `conditions`=%s, `description`=%s, `merchant`=%s,`phone`=%s, `address`=%s,`city`=%s, `country`=%s, `post`=%s",[1,item['site_id'], img,img,0,'',old_pic,small_pic,'',big_pic,item['name'],get_seo_title(item['name']),item['url'],'SGD',item['originalPrice'],item['price'], 0,'reptile',time.time(),item['ExpiryTime'],time.time(),item['website_id'],1,1,1,item['highlight'],item['condition'],item['description'],item['merchant'],item['phone'],item['address'],1,1,item['postCode']])
        return item