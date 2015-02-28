# -*- coding: utf-8 -*-

# Scrapy settings for spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

# BOT_NAME = 'spider'
#
# SPIDER_MODULES = ['spider.spiders']
# NEWSPIDER_MODULE = 'spider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'spider (+http://www.yourdomain.com)'


SPIDER_MODULES = ['spider.spiders']
NEWSPIDER_MODULE = 'spider.spiders'

SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    #'scrapy.contrib.pipeline.images.ImagesPipeline': 1,
    'spider.imagepipelines.MyImagesPipeline': 1,  # zi ding yi tu pian xia zai chu li
    #'spider.imagepipelines.MyImgPipeline':1,  # bu xu yao suo lue tu pian lei
    'spider.pipelines.GoodsPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
    }
IMAGES_STORE = '/wwwroot/dir/uploaded'  # tu pian xia zai mu lu

IMAGES_THUMBS = {
    'thumb100': (100, 100),
    'thumb250': (250, 250),
    'thumb400': (400, 300),
}

DOWNLOAD_DELAY = 0.5    # 250 ms of delay xian su

# sui ji user agent
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
    'spider.rotate_useragent.RotateUserAgentMiddleware' :400
}

# Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Don't cleanup redis queues, allows to pause/resume crawls.
SCHEDULER_PERSIST = True

# Schedule requests using a priority queue. (default)
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

# Schedule requests using a queue (FIFO).
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'

# Schedule requests using a stack (LIFO).
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderStack'

# guang du you xia zai
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'

# Max idle time to prevent the spider from being closed when distributed crawling.
# This only works if queue class is SpiderQueue or SpiderStack,
# and may also block the same time when your spider start at the first time (because the queue is empty).
SCHEDULER_IDLE_BEFORE_CLOSE = 10

# Store scraped item in redis for post-processing.
# ITEM_PIPELINES = [
#     'scrapy_redis.pipelines.RedisPipeline',
# ]

# Specify the host and port to use when connecting to Redis (optional).
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

#LOG_FILE = "./error.log"

# Specify the full Redis URL for connecting (optional).
# If set, this takes precedence over the REDIS_HOST and REDIS_PORT settings.
#REDIS_URL = 'redis://user:pass@hostname:9001'
