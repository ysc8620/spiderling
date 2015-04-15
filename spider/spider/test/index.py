#!/usr/bin/python
#coding=utf-8
import time
import sys,os,json

reload(sys)

sys.setdefaultencoding('utf8')
from scrapy.selector import Selector
from spider.tools.match.parser import *
sys.path.append(sys.path[0]+"/../../")
#from spider.tools.match.myxpath import *
# html_name = './imobshop.sg.html'
# xml_name = 'imobshop.xml'
domain = 'omigo'
html = file(sys.path[0]+'/'+domain+'.html', 'a+').read()
hsl = Selector(text=html)

str_xml = file( sys.path[0]+'/../website/'+domain+'.xml','a+').read()
xsl = Selector(text=str_xml, type='xml')


#<span class='js-time hide
# print hsl.xpath("//div[@id='location']//div[@class='location-address']/text()").extract()
# exit()
# html = html.decode('gb2312')
# js = hsl.xpath("//script[contains(.//text(), 'aImages =')]/text()").re("\[\{.*?\}\]")[0]
# for i in(json.loads(js)):
#     print i['large']
item = sg_parser()
db = DB('test')
items = item.run(text=html, xml=xsl, db=db)

print items
''''''''''''''''''''''''''''''''''''''''''''''''''