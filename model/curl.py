# -*- coding: utf-8 -*-
__author__ = 'ShengYue'
import urllib2
import time
import random
import os.path
import urllib
from log import *
class curl:
    # 链接表
    urlList = {}

    req = None

    #字符编码处理
    def mdcode(self, data, url=''):
        for c in ('utf-8', 'gb2312', 'gbk'):
            try:
                return data.decode(c)
            except Exception, e:
                print (u'编码出错: '+url+', --'+e.message)

        logging.error(u'获取不到编码: '+url+', --'+e.message)

    def read(self,url, config={}):
        try:
            url = urllib.unquote(url)

            header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:19.0) Gecko/20100101 Firefox/19.0'}
            self.req = urllib2.Request(url,headers=header)

            # 添加头信息
            for key in config:
                self.req.add_header(key, config[key])

            res = urllib2.urlopen(self.req)
            html = res.read()
            res.close()

            return self.mdcode(html, url)

        except Exception, e:
            logging.error(u'获取HTML失败:'+url+'--'+e.message)


    def getFileName(self):
        return time.strftime('%y%m%d%H%I',time.localtime(time.time()))+'-'+ str(random.randint(10,99))+'-'+str(random.randint(10,99))

    def down(self,url, path=''):

        ext = os.path.splitext(url)[-1]
        socket = urllib2.urlopen(url)
        data = socket.read()
        fileName =self.getFileName()+ext
        with open( './images/'+fileName, "wb") as jpg:
            jpg.write(data)
        socket.close()

        return '/uploads/images/'+fileName
