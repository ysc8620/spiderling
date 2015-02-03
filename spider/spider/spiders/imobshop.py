#-*-codeing:utf-8-*-
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from spider.items import DealItem
from scrapy.utils.response import get_base_url
import urlparse
import time
import hashlib
import re

class DmozSpider(CrawlSpider):
    name = 'imobshop'
    allowed_domains = ['imobshop.sg']
    start_urls = ['https://www.imobshop.sg']
    website_url = 'imobshop.sg'

    rules = (
        Rule(LinkExtractor(allow=r"https://www.imobshop.sg/$", deny=r".*?(model=list|dir=)")),
        #Rule(LinkExtractor(allow=r"http://www.lazada.sg/.+/(\?page=\d+)?$", deny=r".*?(new\-products|top\-sellers|special\-price)")),
        Rule(LinkExtractor(allow=r"https://www.imobshop.sg/(fun|tech|wellness|food|tavel|home|family|fashion)(/(indoo|outdoo|compute-accessoies|camea-accessoies|mobile-accessoies|skin-cae|cosmetics|accessoies|beauty-sevices|tickets|tavelaccessoies|appliances|watches|household|bags-and-wallets|ladies|men-s))?(\?p=\d+)?$", deny=r".*?(model=list|dir=)")),
        Rule(LinkExtractor(allow=r"https://www.imobshop.sg/(fun|tech|wellness|tavel|home|fashion)/(indoo|outdoo|compute-accessoies|camea-accessoies|mobile-accessoies|skin-cae|cosmetics|accessoies|beauty-sevices|tickets|tavelaccessoies|appliances|watches|household|bags-and-wallets|ladies|men-s)/.+$"), callback='parse_item'),
        Rule(LinkExtractor(allow=r"https://www.imobshop.sg/(family|food)/.+$"), callback='parse_item'),
    )
    def parse_item(self, response):
        hs = Selector(response)
        base_url = get_base_url(response)
        imgs = []

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
        item['price'] = '' if len(price)<1 else price[0].strip().replace('S$','').strip()

        original_price = hs.xpath('//p[@class="special-price"]//span[@class="price"]/text()').extract()
        item['originalPrice'] = '' if len(original_price)<1 else original_price[0].strip().replace('S$','').strip()

        img_list = hs.xpath('//div[contains(@class,"default-views")]//li/a/@href').extract()

        for i in img_list:
            imgs.append(urlparse.urljoin(base_url, i.strip()))

        # if imgs:
        #     item['img'] = imgs[0]

        item['url'] = response.url
        item['countBought'] = 0
        item['website_id'] = 76
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
        address = '' if len(address)<1 else address[0].strip()
        item['address'] = address

        postCode = hs.xpath('//div[@id="product_tabs_additional_contents"]//th[contains(.//text(), "Seller Postal Code")]/ancestor::tr/td/text()').extract()
        postCode = '' if len(postCode)<1 else postCode[0].strip()
        item['postCode'] = postCode

        merchant = hs.xpath('//div[@id="product_tabs_additional_contents"]//th[contains(.//text(), "Seller Name")]/ancestor::tr/td/text()').extract()
        merchant = '' if len(merchant)<1 else merchant[0].strip()
        item['merchant'] = merchant

        phone = hs.xpath('//div[@id="product_tabs_additional_contents"]//th[contains(.//text(), "Seller Phone")]/ancestor::tr/td/text()').extract()
        phone = '' if len(phone)<1 else phone[0].strip()
        item['phone'] = phone

        item['oldImg'] = imgs
        item['descOldImg'] = imgs

        item['image_urls'] = imgs

        return item
