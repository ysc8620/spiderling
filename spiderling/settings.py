# -*- coding: utf-8 -*-

# Scrapy settings for spiderling project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'spiderling'

SPIDER_MODULES = ['spiderling.spiders']
NEWSPIDER_MODULE = 'spiderling.spiders'
#ITEM_PIPELINES = {'spiderling.pipelines.SpiderlingPipeline':1}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'spiderling (+http://www.yourdomain.com)'
