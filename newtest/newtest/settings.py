# Scrapy settings for newtest project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'newtest'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['newtest.spiders']
NEWSPIDER_MODULE = 'newtest.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
ITEM_PIPELINES=['newtest.pipelines.SQLStorePipeline']

