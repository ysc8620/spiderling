#-*-coding:utf-8-*-
from scrapy.selector import Selector
html = open('lazada.html', 'rb').read()
hs = Selector(text=html)
print hs.xpath("//title/text()").extract()[0]