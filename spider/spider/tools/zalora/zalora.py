#-*-coding:utf-8-*-

from scrapy.utils.response import get_base_url
from scrapy.selector import Selector
from spider.items import GoodsItem
import time
import urlparse
import hashlib
import re

html = file('info.html', 'rb').read()
hs = Selector(text=html)


'''
商品结构
_id,  unique_id(唯一编号 md5(website + website_goods_id )), title, price, original_price, img,
img_list( 数组 多图片), brand, category, category_list(数组 分类组合)
description, from_url, from_website(来自网站), status(1默认显示， 2 隐藏，), add_time, update_time
'''

url = 'http://www.zalora.sg/Sheer-Panel-Party-Dress-213757.html'
item = GoodsItem()

url_id = re.match(r'.*?(\d+)\.html', url)
if url_id:
    id = url_id.group(1)
    item['unique_id'] = hashlib.sha1(id).hexdigest()
else:
    pass #open('error.log','rb').write(url+"\r")

title = hs.xpath('//div[contains(@class,"product__title")]/text()').extract()
item['title'] = '' if len(title)<1 else title[0].strip()

price = hs.xpath('//span[contains(@class, "prd-price")]/text()').extract()
price = '' if len(price)<1 else price[0].strip()
if price:
    price = price.replace('SGD','').strip()
    item['price'] = price

# original_price = hs.xpath('//span[@id="price_box"]/text()').extract()
# original_price = '' if len(original_price)<1 else original_price[0].strip()
# if original_price:
#     original_price = original_price.replace('SGD ','').replace(',','').strip()
#     item['original_price'] = original_price

img_list = hs.xpath('//li[contains(@class,"js-swiper-slide")]//img/@src').extract()
#base_url = get_base_url(url)
base_url = 'http://www.lazada.sg/'
imgs = []
item['img'] = ''
item['img_list'] = ''
if img_list:
    for i in img_list:
        r = re.match(r"http://.*?(http://.*?)$", i)
        imgs.append(urlparse.urljoin(base_url, r.group(1).strip()))
    item['img'] = imgs[0]
    item['img_list'] = imgs

item['from_url'] = url

brand = hs.xpath('//div[contains(@class,"product__brand")]//a/text()').extract()
item['brand'] = '' if len(brand)<1 else brand[0].strip()

description = hs.xpath('//div[@id="productDetails"]').extract()
description = '' if len(description)<1 else description[0].strip()
if description:
    description = re.subn(r"\s+"," ",description)[0]
    item['description'] = description
    #description = re.subn(r'<(div).*?>([\s\S]*?)<\/(div)>',r"\2",description)[0]

# description_imgs = hs.xpath('//div[@id="productDetails"]//img/@src').extract()
# if description_imgs:
#     for img in description_imgs:
#         imgs.append(urlparse.urljoin(base_url, img.strip()))

# cate
category = hs.xpath('//li[contains(@class,"prs")]//a/span/text()').extract()
item['category_list'] = category
item['category'] = '' if len(category)<1 else category[len(category)-1].strip()

item['from_website'] = 'zalora.sg'
item['add_time'] = str(int(time.time()))
item['update_time'] = str(int(time.time()))
item['status'] = "1"

item['image_urls'] = imgs

print item