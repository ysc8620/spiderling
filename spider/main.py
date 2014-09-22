#-*-coding:utf-8-*-
__author__ = 'Administrator'

# http://news.cnblogs.com
#from scrapy.contrib.pipeline.media import MediaPipeline

from scrapy.utils.response import get_base_url
import urlparse
import hashlib
import re


from scrapy.selector import Selector
from PIL import Image
import urllib2

#import pymongo

url = '<div class="prd-description"> <div class="xxx">xxx</div>aaa</div><div class="prd-description"> ssss</div>'
p = re.compile(r'<div.*?>([\s\S]*?)<\/div>',re.I)
print p.sub(r'\1', url)
# from pymongo import Connection #导入模块
# con = Connection()
# db = con.test #连接test数据库
# #posts = db.post #连接test中的post集合，相当于MySQL中的表
# db.test.insert({"name":"test"})
# data =  db.test.find()
# for i in data:
#     print i

################################ 解析测试
# response = urllib2.urlopen('http://www.asos.cn/p/543549-MU1')
# html = response.read()
# # print html
#
# hts = Selector(text=html)
# price = hts.xpath("//p[@class='big-price']/text()").extract()[0].strip()#.re(r"(\w+)")
# #price = price.strip().re(r'¥(\w+)')
# print price
################################

# img = Image.open('d:/032125408443538.png')
# img.save('d:/1.jpg', format="jpeg")
#
# url =  'http://images.cnitblog.com/news/157064/201409/032125408443538.png'
# print hashlib.sha1(url).hexdigest()

# print urlparse.urljoin('http://news.blogs.com/test/tess/', '../aa/im.php');
# parsedTuple = urlparse.urljoin("http://www.google.com/search?hl=en&q=python&btnG=Google+Search", 'img.jpg')
# print parsedTuple