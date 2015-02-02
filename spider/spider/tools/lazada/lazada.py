#-*-coding:utf-8-*-

from scrapy.utils.response import get_base_url
from scrapy.selector import Selector
from spider.items import GoodsItem
from datetime import datetime
import urlparse
import hashlib
import re

html = file('test.html', 'rb').read()
hs = Selector(text=html)
import json
import time
from pymongo import Connection


con = Connection('localhost', 27017)
db = con.test
posts = db.goods

#posts.remove()
res = posts.find()
print res.count()
exit()




'''
商品结构
_id,  unique_id(唯一编号 md5(website + website_goods_id )), title, price, original_price, img,
img_list( 数组 多图片), brand, category, category_list(数组 分类组合)
description, from_url, from_website(来自网站), status(1默认显示， 2 隐藏，), add_time, update_time
'''

url = 'http://www.lazada.sg/zwilling-ja-henckels-twin-pollux-6pc-knife-block-set-43836.html'
item = GoodsItem()

url_id = re.match(r'.*?(\d+)\.html', url)
if url_id:
    id = url_id.group(1)
    item['unique_id'] = hashlib.sha1(id).hexdigest()
else:
    open('error.log','rb').write(url+"\r")

title = hs.xpath('//h1[@id="prod_title"]/text()').extract()
item['title'] = '' if len(title)<1 else title[0].strip()

price = hs.xpath('//span[@id="product_price"]/text()').extract()
item['price'] = '' if len(price)<1 else price[0].strip()

original_price = hs.xpath('//span[@id="price_box"]/text()').extract()
original_price = '' if len(original_price)<1 else original_price[0].strip()
if original_price:
    original_price = original_price.replace('SGD ','').replace(',','').strip()
    item['original_price'] = original_price

img_list = hs.xpath('//span[contains(@data-image-key, "gallery")]/@data-swap-image').extract()

#base_url = get_base_url(url)
base_url = 'http://www.lazada.sg/'
imgs = []
for i in img_list:
    imgs.append(urlparse.urljoin(base_url, i.strip()))
item['img'] = imgs[0]

item['from_url'] = url

brand = hs.xpath('//div[@id="prod_brand"]/a[1]/text()').extract()
item['brand'] = '' if len(brand)<1 else brand[0].strip()

description = hs.xpath('//div[@id="productDetails"]').extract()
description = '' if len(description)<1 else description[0].strip()
if description:
    description = re.subn(r"\s+"," ",description)[0]
    item['description'] = description
    #description = re.subn(r'<(div).*?>([\s\S]*?)<\/(div)>',r"\2",description)[0]

description_imgs = hs.xpath('//div[@id="productDetails"]/img/@src').extract()
if description_imgs:
    for img in description_imgs:
        imgs.append(urlparse.urljoin(base_url, img.strip()))

# cate
category = hs.xpath('//div[contains(@class,"header__breadcrumb__wrapper")]//a/span/text()').extract()
item['category_list'] = category
item['category'] = '' if len(category)<1 else category[len(category)-1].strip()

item['from_website'] = 'lazada.sg'
item['add_time'] = datetime.utcnow()
item['update_time'] = datetime.utcnow()
item['status'] = 1

item['image_urls'] = imgs
newitem = {}
newitem['title'] = item['title']
newitem['img_list'] = item['image_urls']
newitem['add_time'] = item['add_time']
posts.insert( newitem)