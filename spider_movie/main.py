#coding=utf-8
__author__ = 'Administrator'

# http://news.cnblogs.com
#from scrapy.contrib.pipeline.media import MediaPipeline
import os

os.chdir(os.getcwd())
print os.system("scrapy crawl dmoz -a n=xxx")
