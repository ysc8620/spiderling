#!/usr/bin/python
#coding=utf-8
import time
import sys,os,json
from spider.tools.db import *

reload(sys)

sys.setdefaultencoding('utf8')
from scrapy.selector import Selector
from spider.tools.match.parser import *
sys.path.append(sys.path[0]+"/../../")
#from spider.tools.match.myxpath import *
# html_name = './imobshop.sg.html'
# xml_name = 'imobshop.xml'
domain = 'qoo10'

html = file(sys.path[0]+'/'+domain+'.html', 'a+').read()
hsl = Selector(text=html)

str_xml = file( sys.path[0]+'/../website/'+domain+'.xml','a+').read()
xsl = Selector(text=str_xml, type='xml')

# fields = xsl.xpath('//targets//model//field')
# for field in fields:
#     print field.xpath('@name').extract()[0]
#     parsers = field.xpath('parsers/parser')
#     #print field.extract()
#     for parser in parsers:
#         print parser.extract()
# exit()
#<span class='js-time hide
print hsl.xpath("//div[@class='goods_detail']//dl[@class='detailsArea']//dt[contains(.//text(), 'Retail Price')]/ancestor::*/dd/text()").extract()
# exit()
# html = html.decode('gb2312')
# js = hsl.xpath("//script[contains(.//text(), 'aImages =')]/text()").re("\[\{.*?\}\]")[0]
# for i in(json.loads(js)):
#     print i['large']
item = test_parser('test')
db = DB('test')
items = item.run(text=html, xml=xsl)

print items
''''''''''''''''''''''''''''''''''''''''''''''''''