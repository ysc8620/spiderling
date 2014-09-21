#-*-codeing:utf-8-*-
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from spider.items import GoodsItem
from scrapy.utils.response import get_base_url
import urlparse

class DmozSpider(CrawlSpider):
    name = 'dmoz'
    allowed_domains = ['news.cnblogs.com']
    start_urls = ['http://news.cnblogs.com/']

    rules = (
        Rule(LinkExtractor(allow=r'http://news.cnblogs.com/n/page/\d+/')),
        Rule(LinkExtractor(allow=r'http://news.cnblogs.com/n/\d+/'), 'parse_item')
    )

    def parse_item(self, response):

        hxs = Selector(response)
        #MyItems = MyItem()
        base_url = get_base_url(response)
        st =  [urlparse.urljoin(base_url, ul) for ul in hxs.xpath('//img/@src').extract()]

        el = GoodsItem()

        el['name']= response.url
        el['description']= response.url
        el['link']= response.url
        el['url']= response.url
        el['image_urls'] = st

        return el
