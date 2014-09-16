__author__ = 'Administrator'

# http://news.cnblogs.com
#from scrapy.contrib.pipeline.media import MediaPipeline
#import lxml.
from scrapy.utils.response import get_base_url
import urlparse
import hashlib


url =  'http://images.cnitblog.com/news/66372/201409/161707074409866.jpg'
print hashlib.sha1(url).hexdigest()

# print urlparse.urljoin('http://news.blogs.com/test/tess/', '../aa/im.php');
# parsedTuple = urlparse.urljoin("http://www.google.com/search?hl=en&q=python&btnG=Google+Search", 'img.jpg')
# print parsedTuple