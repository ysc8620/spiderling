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

class DmozSpider(CrawlSpider):
    name = 'zalora'
    allowed_domains = ['zalora.sg']
    start_urls = ['http://www.zalora.sg/women/all-products/']
    website_url = 'zalora.sg'

    rules = (
        #http://www.zalora.sg/women/all-products/?sort=popularity&dir=desc&page=2
        #Rule(LinkExtractor(allow=r"http://www.zalora.sg/$"),
        Rule(LinkExtractor(allow=r"^http://www.zalora.sg/women/all-products/$")),
        Rule(LinkExtractor(allow=r"^http://www.zalora.sg/women/all-products/\?sort=popularity&dir=desc&page=(\d+)$")),
        Rule(LinkExtractor(allow=r"^http://www.zalora.sg/[^\/]+?\d+\.html"), callback='parse_item')
    )
    def parse_item(self, response):
        hs = Selector(response)
        base_url = get_base_url(response)
        imgs = []

        item = GoodsItem()

        url_id = re.match(r'.*?(\d+)\.html', response.url)
        if url_id:
            id = url_id.group(1)
            item['unique_id'] = hashlib.sha1(id).hexdigest()
        else:
            pass #open('error.log','rb').write(response.url+"\r")

        title = hs.xpath('//div[contains(@class,"product__title")]/text()').extract()
        item['title'] = '' if len(title)<1 else title[0].strip()

        price = hs.xpath('//span[contains(@class, "prd-price")]/text()').extract()
        price = '' if len(price)<1 else price[0].strip()
        if price:
            price = price.replace('SGD','').strip()
            item['price'] = price

        item['original_price'] = '0'
        original_price = hs.xpath('//span[@id="price_box"]/text()').extract()
        original_price = '' if len(original_price)<1 else original_price[0].strip()
        if original_price:
            original_price = original_price.replace('SGD ','').replace(',','').strip()
            item['original_price'] = original_price

        img_list = hs.xpath('//li[contains(@class,"js-swiper-slide")]//img/@src').extract()
        #base_url = get_base_url(url)
        #base_url = 'http://www.lazada.sg/'
        #imgs = []
        item['img'] = ''
        item['img_list'] = ''
        if img_list:
            for i in img_list:
                r = re.match(r"http://.*?(http://.*?)$", i)
                imgs.append(urlparse.urljoin(base_url, r.group(1).strip()))
            item['img'] = imgs[0]
            item['img_list'] = imgs

        item['from_url'] = response.url

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

        return item

