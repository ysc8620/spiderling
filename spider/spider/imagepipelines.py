#-*-coding:utf-8-*-

from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem
import hashlib

class MyImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        #image_guid = request.url.split('/')[-1]
        image_guid = hashlib.sha1(request.url).hexdigest()
        path = image_guid[0:2]
        return 'original/%s/%s.jpg' % (path, image_guid)

    # 缩略图路径
    def thumb_path(self, request, thumb_id, response=None, info=None):
        image_guid = hashlib.sha1(request.url).hexdigest()
        path = image_guid[0:2] #thumbs
        #return 'full/%s%s.jpg' % (path, image_guid)
        #thumb_guid = hashlib.sha1(request.url).hexdigest()  # change to request.url after deprecation
        return '%s/%s/%s.jpg' % (thumb_id,path, image_guid)

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item
