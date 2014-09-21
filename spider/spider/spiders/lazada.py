#-*-codeing:utf-8-*-
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from spider.items import GoodsItem
from scrapy.utils.response import get_base_url
import urlparse

class DmozSpider(CrawlSpider):
    name = 'lazada'
    allowed_domains = ['lazada.sg']
    start_urls = ['http://www.lazada.sg/']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.lazada.sg/\S+')),
        Rule(LinkExtractor(allow=r'http://www.lazada.sg/[\w\-]+\d+\.html/'), 'parse_item')
    )

    def parse_item(self, response):

        hxs = Selector(response)
        #MyItems = MyItem()
        base_url = get_base_url(response)
        st =  [urlparse.urljoin(base_url, ul) for ul in hxs.xpath('//img/@src').extract()]

        el = GoodsItem()

        el['title']= response.url
        el['description']= response.url
        el['link']= response.url
        el['url']= response.url
        el['image_urls'] = st

        return el
