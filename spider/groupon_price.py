#!/usr/bin/python
#coding=utf-8
import os, sys,json
import requests,time,re
from spider.tools.db import *
from spider.tools.SimpleClassifier import SimpleClassifier
from scrapy.selector import Selector
reload(sys)
sys.setdefaultencoding('utf8')
website_id=5
db = DB('sg')
Classifier = SimpleClassifier('sg')

while True:
    r = requests.session()
    res = db.execute("SELECT goods_id,url FROM le_goods WHERE website_id=5 AND price=0 AND seller_user_id=0")
    row = res.fetchone()
    if row == None:
        break
    data = r.get(row['url'],params={})

    hsl = Selector(text=data.text.decode('utf8', 'replace'))
    reprice = hsl.xpath("//span[@class='noWrap']/text()").extract()
    hsl = Selector(text=data.text.decode('utf8', 'replace'))
    reprice_old = hsl.xpath("//span[@class='savings2_cell savings2_saving']//span[@class='savings2_values']/text()").extract()
    price = 0
    if reprice:
        price = reprice[0].replace('S$','').replace(',','')
        print price,'-'

    price_old = 0
    if reprice_old:
        price_old = reprice_old[0].replace('S$','').replace(',','')
        print price_old,'='

    db.execute("UPDATE le_goods SET seller_user_id=1,original_price=%s,price=%s WHERE goods_id=%s",[price_old,price,row['goods_id']])
    time.sleep(10)

