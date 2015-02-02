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
        open('imobshop.log','a+').write(response.url+"\r\n")
        hs = Selector(response)
        base_url = get_base_url(response)
        imgs = []

        item = DealItem()
        url_id = re.match(r'.*?(\d+)\.html', response.url)
        if url_id:
            id = url_id.group(1)
            item['unique_id'] = hashlib.sha1(self.website_url + id).hexdigest()
        else:
            pass#open('error.log','rb').write(response.url+"\r")

        title = hs.xpath('//h1[@id="prod_title"]/text()').extract()
        item['title'] = '' if len(title)<1 else title[0].strip()

        price = hs.xpath('//span[@id="product_price"]/text()').extract()
        item['price'] = '' if len(price)<1 else price[0].strip()

        original_price = hs.xpath('//span[@id="price_box"]/text()').extract()
        original_price = '' if len(original_price)<1 else original_price[0].strip()
        if original_price:
            original_price = original_price.replace('SGD ','').replace(',','').strip()
            item['original_price'] = original_price

        item['img'] = ''
        item['img_list'] = ''
        img_list = hs.xpath('//span[contains(@data-image-key, "gallery")]/@data-swap-image').extract()
        if img_list:
            for i in img_list:
                imgs.append(urlparse.urljoin(base_url, i.strip()))
            item['img'] = imgs[0]
            item['img_list'] = imgs

        item['from_url'] = response.url

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
        bool = False
        if category:
            for c in category:
                if( c == 'Fashion' or c=='Women' or c=='Womens'):
                    bool = True
        if bool == False :
            item['title'] = ''

        item['from_website'] = self.website_url
        item['add_time'] = str(int(time.time()))
        item['update_time'] = str(int(time.time()))
        item['status'] = 1

        item['image_urls'] = imgs

        return item
