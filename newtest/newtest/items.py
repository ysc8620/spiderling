# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class TorrentItem(Item):
    # define the fields for your item here like:
    # name = Field()
    #`id`, `original_id`, `name`, `brand`, `price`, `original_price`, `weight`, `description`, `from_url`, `website_id`, `update_time`, `addtime`
    original_id = Field()
    name = Field()
    img = Field()
    brand = Field()
    price = Field()
    original_price = Field()
    #weight = Field()
    description = Field()
    from_url = Field()
    website_id = Field()
