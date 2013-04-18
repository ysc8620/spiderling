# -*- coding: utf-8 -*-
__author__ = 'ShengYue'
import urllib2
import time
import random
import os.path
import urllib
from log import log
class curl:
    # 链接表
    urlList = {}

    req = None

    #字符编码处理
    def mdcode(self, data):
       # code = chardet.detect(data)
        #return data.decode(code['encoding'])
        for c in ('utf-8', 'gbk', 'gb2312'):
            try:
                return data.decode(c)
            except:
                pass
#
#        for c in ('utf-8', 'gbk', 'gb2312'):
#            try:
#                return data.encode( 'utf-8' )
#            except:
#                pass
#
#        return data
    #
    def getBaseUrl(self, base_url, link):
        print ''

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

            # code = chardet.detect(html)
            return self.mdcode(html)

        except:
            print u'获取HTML失败'
            return ''

    def getFileName(self):
        return time.strftime('%y%m%d%H%I',time.localtime(time.time()))+'-'+ str(random.randint(10,99))+'-'+str(random.randint(10,99))

    def down(self,url):

        ext = os.path.splitext(url)[-1]
        socket = urllib2.urlopen(url)
        data = socket.read()
        fileName =self.getFileName()+ext
        with open( './images/'+fileName, "wb") as jpg:
            jpg.write(data)
        socket.close()

        return '/uploads/images/'+fileName
