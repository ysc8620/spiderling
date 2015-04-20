__author__ = 'ShengYue'
#!/usr/bin/python
#coding=utf-8
import sys,os
import time, datetime, math
from inflector import *
from spider.tools.db import *
from spider.tools.common import get_title
reload(sys)
sys.setdefaultencoding('utf8')

class StatisticClassifier:

    def classifyByName(self, name):
        title = get_simple_text(name)
        ids = self.fetchCateIdByName(title)
        count = self.staticByCateId(ids)
        max = 0
        cateId = -1
        for i in range(count):
            value = count[i]['cate_id']
            if(value > max):
                max = value
                cateId = count[i]['cate_id']
		return cateId

    def fetchCateIdByName(self, name):
        pass

    def staticByCateId(self, ids):
        pass
       # cateMap = {}
		# for id in ids:
		# 	Integer obj=(Integer)cateMap.get(id);
		# 	if(obj==null){
		# 		cateMap.put(id, 1);
		# 	}else{
		# 		cateMap.put(id,obj.intValue()+1);
		# 	}
       #
		# return cateMap;
