# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, TakeFirst, Join

'''
商品结构
_id,  unique_id(唯一编号 md5(website + website_goods_id )), title, price, original_price, img,
img_list( 数组 多图片), brand, category, category_list(数组 分类组合)
description, from_url, from_website(来自网站), status(1默认显示， 2 隐藏，), add_time, update_time
'''
class GoodsItem(Item):
    unique_id = Field()
    title = Field()
    price = Field()
    original_price = Field()
    img = Field()
    img_list = Field()
    brand = Field()
    category = Field()
    category_list = Field()
    from_url = Field()
    from_website = Field()
    status = Field()
    add_time = Field()
    update_time = Field()
    description = Field()

    # 系统自动图片下载处理
    image_urls = Field()
    images = Field()


class ExampleLoader(ItemLoader):
    default_item_class = GoodsItem
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()
     # ... other item fields ...
    image_urls = Field()
    images = Field()