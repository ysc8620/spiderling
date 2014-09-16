#-*-codeing:utf-8-*-
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from example.items import ExampleItem

class DmozSpider(CrawlSpider):
    name = 'dmoz'
    allowed_domains = ['news.cnblogs.com']
    start_urls = ['http://news.cnblogs.com/']

    rules = (
        Rule(LinkExtractor(allow=r'http://news.cnblogs.com/n/page/\d+/')),
        Rule(LinkExtractor(allow=r'http://news.cnblogs.com/n/\d+/'), 'parse_item')
    )

    # def parse(self, response):
    #     hxs = Selector(response)
    #     MyItems = MyItem()
    #     ins = hxs.xpath('//img/@src').extract()
    #     st = []
    #     for s in ins:
    #         st.append("http://news.cnblogs.com/"+s)
    #     MyItems['image_urls'] = st
    #     return MyItems

    #     open('img.log','a+').write(li+'\r\n')

    def parse_item(self, response):
        hxs = Selector(response)
        #MyItems = MyItem()
        ins = hxs.xpath('//img/@src').extract()
        st = []
        for s in ins:
            st.append("http://news.cnblogs.com/"+s)

        el = ExampleItem()

        el['name']= response.url
        el['description']= response.url
        el['link']= response.url
        el['url']= response.url
        el['image_urls'] = st

        return el
