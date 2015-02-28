#-*-coding:utf-8-*-

from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem
import hashlib
from cStringIO import StringIO
from PIL import Image
import time
## dd/mm/yyyy格式
#print (time.strftime("%d/%m/%Y"))

#TODO: from scrapy.contrib.pipeline.media import MediaPipeline
from scrapy.contrib.pipeline.files import FileException, FilesPipeline

class ImageException(FileException):
    """General image error exception"""

class MyImgPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        #image_guid = request.url.split('/')[-1]
        image_guid = hashlib.sha1(request.url).hexdigest()
        path = image_guid[0:2]
        return 'original/%s/%s/%s/%s.jpg' % (path,time.strftime("%Y"),time.strftime("%m%d"), image_guid)

    def get_images(self, response, request, info):
        path = self.file_path(request, response=response, info=info)
        orig_image = Image.open(StringIO(response.body))

        width, height = orig_image.size
        if width < self.MIN_WIDTH or height < self.MIN_HEIGHT:
            raise ImageException("Image too small (%dx%d < %dx%d)" %
                                 (width, height, self.MIN_WIDTH, self.MIN_HEIGHT))

        image, buf = self.convert_image(orig_image)
        yield path, image, buf

    def get_media_requests(self, item, info):
        for image_url in item['img_urls']:
            yield Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item
