#-*-coding:utf-8-*-

from scrapy.utils.response import get_base_url
from scrapy.selector import Selector
from spider.items import DealItem
from datetime import datetime
import urlparse
import hashlib
import re

html = file('imobshop.html', 'rb').read()
hs = Selector(text=html)
import json
import time
from pymongo import Connection


# con = Connection('localhost', 27017)
# db = con.test
# posts = db.goods
#
# #posts.remove()
# res = posts.find()
# print res.count()
# exit()




'''
商品结构
_id,  unique_id(唯一编号 md5(website + website_goods_id )), title, price, original_price, img,
img_list( 数组 多图片), brand, category, category_list(数组 分类组合)
description, from_url, from_website(来自网站), status(1默认显示， 2 隐藏，), add_time, update_time
'''

url = 'https://www.imobshop.sg/fun/indoor/k-box-3-hrs-singing-package'
item = DealItem()

# url_id = hs.xpath('//input[@name="product"]/@value').extract()
# if url_id:
#     id = url_id[0].strip()
#     item['unique_id'] = hashlib.sha1(id).hexdigest()
# else:
#     pass


title = hs.xpath('//div[@class="product-name"]/h1/text()').extract()
item['name'] = '' if len(title)<1 else title[0].strip()

price = hs.xpath('//p[@class="special-price"]//span[@class="price"]/text()').extract()
item['price'] = '' if len(price)<1 else price[0].strip().replace('S$ ','').strip()

original_price = hs.xpath('//p[@class="special-price"]//span[@class="price"]/text()').extract()
item['originalPrice'] = '' if len(original_price)<1 else original_price[0].strip().replace('S$ ','').strip()

img_list = hs.xpath('//div[contains(@class,"default-views")]//li/a/@href').extract()
print img_list
#base_url = get_base_url(url)
base_url = 'https://www.imobshop.sg/'
imgs = []
for i in img_list:
    imgs.append(urlparse.urljoin(base_url, i.strip()))

# if imgs:
#     item['img'] = imgs[0]

item['url'] = url
item['countBought'] = 0
item['ExpiryTime'] = int(time.time()) + 2592000

description = hs.xpath('//div[@id="product_tabs_description_contents"]').extract()
description = '' if len(description)<1 else description[0].strip()
if description:
    description = re.subn(r"\s+"," ",description)[0]
    item['description'] = description
    #description = re.subn(r'<(div).*?>([\s\S]*?)<\/(div)>',r"\2",description)[0]

# cate
category = hs.xpath('//div[@class="breadcrumbs"]//li[contains(@class,"category")]/a/text()').extract()
item['cate'] = '' if len(category)<1 else category[len(category)-1].strip()

item['highlight'] = ''
item['condition'] = ''
#product-attribute-specs-table
address = hs.xpath('//div[@id="product_tabs_additional_contents"]//th[contains(.//text(), "Seller Address")]/ancestor::tr/td/text()').extract()
address = '' if len(address)<1 else address[0].strip().strip()
item['address'] = address

postCode = hs.xpath('//div[@id="product_tabs_additional_contents"]//th[contains(.//text(), "Seller Postal Code")]/ancestor::tr/td/text()').extract()
postCode = '' if len(postCode)<1 else postCode[0].strip().strip()
item['postCode'] = postCode

merchant = hs.xpath('//div[@id="product_tabs_additional_contents"]//th[contains(.//text(), "Seller Name")]/ancestor::tr/td/text()').extract()
merchant = '' if len(merchant)<1 else merchant[0].strip().strip()
item['merchant'] = merchant

phone = hs.xpath('//div[@id="product_tabs_additional_contents"]//th[contains(.//text(), "Seller Phone")]/ancestor::tr/td/text()').extract()
phone = '' if len(phone)<1 else phone[0].strip().strip()
item['phone'] = phone

item['oldImg'] = imgs
item['descOldImg'] = ''

item['image_urls'] = imgs

print item