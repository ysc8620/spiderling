# -*- coding: utf-8 -*-
__author__ = 'ShengYue'

import re
#import SpiderlingItem
#from hamster.items import HamsterItem
# m = re.match(r'/n/page/\d+$/', 'http://news.cnblogs.com/n/page/2/')
from spiderling.spiders.DmozItem import DmozItem

m = re.match(r'http://news.cnblogs.com/n/page/\d+/', 'http://news.cnblogs.com/n/page/2/')

items = []
item = DmozItem()
item['title'] = 'hello'
items.append(item)


#print items[0]
if m:
    print 'ok'
else:
    print 'false'