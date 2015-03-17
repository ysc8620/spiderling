#!/usr/bin/python
#coding=utf-8
from spider.tools.matchfield import match_dmoz_field
from scrapy.selector import Selector
import time
import sys,os
reload(sys)

sys.setdefaultencoding('utf8')
# html_name = './imobshop.sg.html'
# xml_name = 'imobshop.xml'
html_name = './deal.com.sg.html'
xml_name = 'deal.com.sg.xml'
html = file(html_name, 'a+').read()
hsl = Selector(text=html)
print int(time.time())
str_xml = file( '../../spiders/website/'+xml_name,'a+').read()
xsl = Selector(text=str_xml, type='xml')
#<span class='js-time hide
# print hsl.xpath("//div[@id='location']//div[@class='location-address']/text()").extract()
# exit()
item = match_dmoz_field(text=html, xml=xsl)
for i in item:
    if type(item[i]) == unicode or type(item[i]) == str:
        print i
        #item[i] = item[i].encode('utf-8')
''''''''''''''''''''''''''''''''''''''''''''''''''