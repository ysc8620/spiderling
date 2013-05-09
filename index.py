# -*- coding: utf-8 -*-
'''
爬虫引导入口 启用多线程处理该事物
'''
__author__ = 'ShengYue'
import threading
import time
from lxml import etree
import os
from model.log import *
from model.db import *
from model.curl import *
from model.match import *

'''
爬虫调度接口
'''
class newsspider:
    def __init__(self, xpath_file):
        self.xpath_file = xpath_file
        logging.info(u'-----------------------------------------------------------------------------')
        logging.info(u'创建newsspider对象: '+xpath_file)
        try:
            if os.path.exists(xpath_file):
                self.config_tree = etree.ElementTree(file=xpath_file)
                sites = self.config_tree.xpath('//site')
                if sites == []:
                    logging.error(u'网站配置文件格式不对'+xpath_file)
                    exit(0)

                site = sites[0]

                # 网址获取
                self.site_url = site.get('url')
                if self.site_url == None:
                    logging.error(u'网站配置文件网址获取失败'+xpath_file)
                    exit(0)

                # 网站名
                self.site_name = site.get('siteName')
                self.daily = float(site.get('daily'))

                # 网站链接读取规则
                self.readMode = site.get('readMode')
                print self.readMode

                self.linkRule = self.config_tree.xpath('//linkRules/rule')
                self.infoUrlRule = self.config_tree.xpath('//urlRules/rule')
                self.infoRule = self.config_tree.xpath('//targets/target/model/field')
                self.linkdb = linkdb(self.site_name)

                self.run(self.site_url)
            else:
                logging.error(u'配置文件不存在: '+xpath_file)
                exit(0)
        except Exception, e:
            logging.error(u'读取配置文件失败: '+xpath_file+', --'+e.message)
            exit(0)

    def run(self, url):
        logging.info(u'开始执行配置文件: '+self.xpath_file)
        if self.readMode == 'normal':
            self.autoRead(url)

        elif self.readMode == 'match':
            print u'没有找到匹配模式'
        else:
            logging.error(u'没有找到读取规则'+self.xpath_file)
            exit(0)

    def autoRead(self, url):

        time.sleep(self.daily)
        try:
            # 初次
            if url != None:
                url = self.site_url

            else:
                urlData = self.linkdb.get_url(self.site_name)
                if urlData == None:
                    logging.info(self.url+u'读取成功')
                    exit(0)
                url = urlData[1]

                #更新
                self.linkdb.update_url(urlData[0])

            html = curl().read(url)

            if html == None:
                logging.error(u'获取HTML失败: '+url)

            '''获取链接'''

            self.match = match(html)
            all_links = self.match.get_all_links(self.linkRule, url)
            print all_links

        except Exception, e:
            logging.error(u'执行失败'+self.xpath_file+', --'+e.message)

    def close(self):
        logging.info(u'执行完毕: ')
        self.linkdb.close()


'''
创建线程实例
'''
class timer(threading.Thread): #The timer class is derived from the class threading.Thread
    def __init__(self, num, interval):
        threading.Thread.__init__(self)
        self.thread_num = num
        self.i = 0
        self.interval = interval
        self.thread_stop = False

    def run(self): #Overwrite run() method, put what you want the thread do here
        while not self.thread_stop:
            self.i = self.i+1
            print '%d Thread Object(%d), Time:%s\n' %(self.i, self.thread_num, time.ctime())
            time.sleep(self.interval)
    def stop(self):
        self.thread_stop = True
def test():
    thread1 = timer(1, 0.01)
    thread2 = timer(2, 0.2)
    thread1.start()
    thread2.start()
    newsspider()
    time.sleep(5)
    thread1.stop()
    thread2.stop()
    return

if __name__ == '__main__':
    #test()
    ns = newsspider('yousheng.xml')
    #ns.run()
    ns.close()


