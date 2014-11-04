#-*-codeing:utf-8-*-
from scrapy.selector import Selector
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from spider.items import GoodsItem
from scrapy.utils.response import get_base_url
import urlparse
import time
import hashlib
import re
from spider.tools import common

class DmozSpider(CrawlSpider):
    name = 'asos'
    allowed_domains = ['asos.cn']
    start_urls = ['http://www.asos.cn/women']
    website_url = 'zalora.sg'

    rules = (
        #http://www.zalora.sg/women/all-products/?sort=popularity&dir=desc&page=2
        #Rule(LinkExtractor(allow=r"http://www.zalora.sg/$"),
        Rule(LinkExtractor(allow=r"^http://www.zalora.sg/women/$")),
        Rule(LinkExtractor(allow=r"^http://www.zalora.sg/women/.+?/$")),
        Rule(LinkExtractor(allow=r"^http://www.zalora.sg/women/.+?/\?sort=popularity&dir=desc&page=(\d+)$")),
        Rule(LinkExtractor(allow=r"^http://www.zalora.sg/[^\/]+?\d+\.html"), callback='parse_item')
    )
    def parse_item(self, response):
        hs = Selector(response)
        base_url = get_base_url(response)
        imgs = []

        item = GoodsItem()
        item['from_website'] = 'asos.cn'
        url_id = re.match(r'.*?(\d+)-(\w+?)', response.url)
        if url_id:
            id = url_id.group(1)
            item['unique_id'] = hashlib.sha1(id).hexdigest()
        else:
            common.logs('id zero:'+item['from_website']+','+response.url)

        title = hs.xpath('//div[@id="productDetailUpdateable"]//h1/text()').extract()
        item['title'] = '' if len(title)<1 else title[0].strip()

        item['price'] = '0'

        if item['price'] == '0':
            price = hs.xpath('//p[contains(@class, "big-price")]/text()').extract()
            price = '' if len(price)<1 else price[0].strip()

            if price:
                #item['price'] = price.replace( re.compile(r".+?([0-9\.]+)"),"x")
                res = re.match(r"^.+?([0-9\.]+).*?",price)
                if res:
                    item['price'] = res.group(1)

        # if item['price'] == '0':
        #     price = hs.xpath('//span[contains(@class, "prd-price")]/text()').extract()
        #     price = '' if len(price)<1 else price[0].strip()
        #
        #     if price:
        #         price = price.replace('SGD','').strip()
        #         item['price'] = price

        if item['price'] == '0':
            common.logs(item['from_website']+","+response.url);

        # original_price = hs.xpath('//span[@id="price_box"]/text()').extract()
        # original_price = '' if len(original_price)<1 else original_price[0].strip()
        # if original_price:
        #     original_price = original_price.replace('SGD ','').replace(',','').strip()
        #     item['original_price'] = original_price

        img_list = hs.xpath('//div[contains(@class,"img_container")]/img/@src').extract()
        #base_url = get_base_url(url)
        base_url = 'http://images.asos.cn/'
        imgs = []
        item['img'] = ''
        item['img_list'] = ''
        if img_list:
            for i in img_list:
                #r = re.match(r"http://.*?(http://.*?)$", i)
                imgs.append(urlparse.urljoin(base_url,i.strip()))
            item['img'] = imgs[0]
            item['img_list'] = imgs

        item['from_url'] = response.url

        brand = hs.xpath('//div[@id="b"]//a/text()').extract()
        item['brand'] = '' if len(brand)<1 else brand[0].strip()

        description = hs.xpath('//div[@id="tab-details"]').extract()
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
        category = hs.xpath('//div[contains(@class,"breadcrumb")]//a/text()').extract()
        item['category_list'] = category
        item['category'] = '' if len(category)<1 else category[len(category)-1].strip()


        item['add_time'] = str(int(time.time()))
        item['update_time'] = str(int(time.time()))
        item['status'] = "1"

        item['image_urls'] = imgs
        return item

