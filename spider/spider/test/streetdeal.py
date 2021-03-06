#!/usr/bin/python
#coding=utf-8
import os, sys,json
import requests,time,re
from spider.tools.db import *
from spider.tools.SimpleClassifier import SimpleClassifier
from scrapy.selector import Selector
from spider.tools.match.parser import *
reload(sys)
sys.setdefaultencoding('utf8')
website_id=5

db = DB('sg')
Classifier = SimpleClassifier('sg')
sess = requests.session()

def add_cate_goods_index( cate_id, goods_id):
    db.execute("INSERT INTO le_cate_goods_index SET cate_id=%s, goods_id=%s,weight=0",[cate_id, goods_id])
g_time = 0
for i in range(0,3):

    url = 'http://www.streetdeal.sg/home/rss/9024913/0/0/0/0/'+i+'/1?utm_source=aggregators&utm_medium=ilovedeals&utm_campaign=9000425'
    data = sess.get(url,params={})
    data = data.text.decode('utf8', 'replace')


    for deal in data:
        #print deal
        item = {}
        #name,countBought,website_id,site_id,price,oldImg,
        #ExpiryTime,highlight,condition,description
        timeStamp = int(time.time())+864000
        # if(len(deal['endAt']) > 1):
        #     timeArray = time.strptime(deal['endAt'], "%Y-%m-%dT%H:%M:%SZ")
        #     #转换为时间戳:
        #     timeStamp = int(time.mktime(timeArray))
        id = ''
        m = re.compile(r'.*?(\d+)$')
        r = m.match(deal['id'])
        if r:
            item['site_id'] = r.groups()[0]
        else:
            item['site_id'] = 0
        item['name'] = deal['title']
        item['countBought'] = 0
        item['website_id'] = website_id
        item['oldImg'] = deal['grid6ImageUrl']
        item['ExpiryTime'] = timeStamp
        item['highlight'] = deal['highlightsHtml']
        item['condition'] = deal['finePrint']
        item['description'] = deal['pitchHtml']
        item['url'] = deal['dealUrl']
        item['originalPrice'] = 0
        item['price'] = 0
        item['merchant'] = ''
        item['phone'] = ''
        item['address'] = ''
        item['postCode'] = ''

        print item['site_id'], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        for i in item:
            if type(item[i]) == unicode or type(item[i]) == str:
                item[i] = item[i].encode('utf-8')
        try:
            res = db.execute("SELECT goods_id, name, price, original_price,isshow,cate_id FROM le_goods WHERE website_id=%s AND site_id=%s", [website_id,item['site_id']])
            row = res.fetchone()
            if row != None:
                print "Old=",item['site_id'], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                item['goods'] = row
            else:
                print "New=",item['site_id'], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                item['goods'] = False

            if item['goods']:
                goods_cate_id = 0
                # 更新cate_id
                if item['goods']['cate_id'] < 1:
                    classlist = Classifier.findCateAndTags(item['name'], 4)
                    if classlist['cate']:
                        goods_cate_id = classlist['cate']
                        add_cate_goods_index(classlist['cate'], item['goods']['goods_id'])
                        for cate_id in classlist['cates']:
                            add_cate_goods_index(cate_id, item['goods']['goods_id'])
                else:
                    goods_cate_id = item['goods']['cate_id']
                res = db.execute("UPDATE le_goods SET isshow=1,uptime=%s,expiry_time=%s,site_id=%s,cate_id=%s WHERE goods_id=%s",[int(time.time()),item['ExpiryTime'], item['site_id'],goods_cate_id,item['goods']['goods_id']])
                #print res._last_executed
            else:
                classlist = Classifier.findCateAndTags(item['name'], 4)
                goods_cate_id = classlist['cate']

                res = db.execute("INSERT INTO le_goods SET seller_user_id=1,`uid`=%s,`site_id`=%s,`img`=%s, `deal_img`=%s,`display_order`=%s,`desc_bigpic`=%s, `oldimg`=%s, `small_pic`=%s,`desc_oldimg`=%s,`bigpic`=%s, `name`=%s, `seo_title`=%s, `url`=%s, `currency`=%s,`original_price`=%s, `price`=%s, `cate_id`=%s, `source`=%s, `addtime`=%s,`expiry_time`=%s, `uptime`=%s, `website_id`=%s,`isdeal`=%s,`ispublish`=%s,`isshow`=%s,`highlight`=%s, `conditions`=%s, `description`=%s, `merchant`=%s,`phone`=%s, `address`=%s,`city`=%s, `country`=%s, `post`=%s",[1,item['site_id'], '','',0,'',item['oldImg'],'','','',item['name'],get_seo_title(item['name']),item['url'],'SGD',0,0, goods_cate_id,'reptile',time.time(),item['ExpiryTime'],time.time(),item['website_id'],1,1,1,item['highlight'],item['condition'],item['description'],item['merchant'],item['phone'],item['address'],1,1,item['postCode']])
                #print '----'
                #print res._last_executed
                goods_id = res.lastrowid
                if classlist['cate'] > 0:
                    add_cate_goods_index(classlist['cate'],goods_id)
                    for cate_id in classlist['cates']:
                        add_cate_goods_index(cate_id, goods_id)
            time.sleep(1)
        except  Exception, e:
            print e
            print 'error'
