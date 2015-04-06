#!/usr/bin/python
#coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from spider.items import *
from spider.tools.db import DB
from scrapy.selector import Selector
from spider.items import *
from scrapy.utils.response import get_base_url
import urlparse
import time
import re
from spider.tools.common import *

# html = '''
# <div class="product-tabs-content" id="product_tabs_description_contents">    <div class="std">
#         <p style="text-align: justify;"><strong>Enthusiast NVIDIA GeForce GTX 880M discrete graphics card with GDDR5 8GB/4GB VRAM</strong></p>
# <p style="text-align: justify;">The NVIDIA GeForce GTX 880M leverages NVIDIA's revolutionary new architecture to deliver extreme performance than the previous generation. Compare to GeForce GTX 780M, users could get over 21% faster and more performance at same level new graphics card with lower temperature and watts. Turn on lightning-fast antialiasing in a huge variety of games automatically. Get maximum gaming images and best compatibility with NVIDIA graphics. Feel the difference reality with NVIDIA PhysX? technology , bringing games to life with dynamic, interactive environments.</p>
# <p style="text-align: justify;"><strong>The latest 4th generation Intel? Core? i7 Processor</strong></p>
# <p style="text-align: justify;">The latest 4th generation quad core processor platform, representing superior performance over previous generations. The CPU performance has increased by 3%~7%, while the overall platform is 15% more powerful. Additionally, the GPU performance of 2d and 3D visuals, is even more noteworthy, with an average increase of over 30%. There have also been significant advances in user experience and battery life. Moreover, it employs a more advanced encryption program to help businesses enhance information security and to protect your BIOS/FW from attacks by malware.</p>
# <p style="text-align: justify;"><strong>SteelSeries Engine to customize every key and devices for personalizing your play style</strong></p>
# <p style="text-align: justify;">SteelSeries Engine is the Apps to combine all frequent functions for gamers in order to easily customize every individual key and functions to personalize every gamer’s play style, including KLM, multiple devices management (for example, headset, mouse, and keyboard), keypress macros, and text macros.</p>
# <p style="text-align: justify;"><strong>XSplit Gamecaster : The Best Recording &amp; Streaming App for Gamers</strong></p>
# <p style="text-align: justify;">"XSplit Gamecaster lets you easily record your gaming moments and broadcast your live gameplay sessions to Twitch, YouTube, UStream and more.</p>
# <p style="text-align: justify;">It’s simple, easy to use and ideal for sharing your gameplay with friends family, or the world - Or for capturing those perfect gaming moments, just for the heck of it.</p>
# <p style="text-align: justify;">So what are you waiting for? Join the revolution and start streaming and recording with XSplit Gamecaster today."</p>
# <p style="text-align: justify;"><strong>Exclusive Super RAID 2 with 3 SSD RAID gives over 1500MB/s reading speed! (optional)</strong></p>
# <p style="text-align: justify;">"Super RAID 2 design gives the storage performance up to 1500MB/s reading performance on MSI GT series, the reading, writing and saving speeds is 15x faster than a single 750GB 7200rpm HDD.</p>
# <p style="text-align: justify;">And one more HDD can be installed in the same laptop without the need to expand the size to put recovery system, to backup and put more data."</p>
# <p style="text-align: justify;"><strong>Exclusive Cooler Boost 2 technology improves 15% cooling performance with lower noise</strong></p>
# <p style="text-align: justify;">Compare to last generation of Cooler Boost technology on GT series in 2012, MSI Cooler Boost 2 technology make a better balanced design, we use thermal bridge connects both CPU cooling and Graphics cooling system together, once CPU or Graphics is hotter than another side, the bridge could transfer the heat to another side faster, so the cooling performance is over 15% on most usage, chip temperature is 15% lower at same watts, and up to 25% lower noise of the laptop system!</p>
# <p style="text-align: justify;"><strong>The Real Deal: A Keyboard Made Just for Gamers</strong></p>
# <p style="text-align: justify;">Exclusive keyboard position and golden triangle layout to offer faster and longer-lasting keyboard action.</p>
# <p style="text-align: justify;"><strong>Killer? E2200 Game Networking for smarter, faster, networking for all online entertainment</strong></p>
# <p style="text-align: justify;">The benefit of the Killer Gaming LAN is the "Advanced Game Detect?" technology, which recognizes online game data packs and processes them first, accelerating them in the process. The best weapon against stuttering characters, freeze-ups, and lagging, it vastly improves all the online experience. Whether FPS or MMO gaming, you’ll have that advantage to response faster to get victorious.</p>
# <p style="text-align: justify;"><strong>Matrix display expands the vision for extreme gaming experience</strong></p>
# <p style="text-align: justify;">Matrix display features up to 3 external display, allowing you to output to 3 displays simultaneously using HDMI 1.4, mini Display-Port 1.2 and VGA port. Users can work with multi-task at the same time. (Overall 4 monitors include notebook's monitor on GT series).</p>
# <p style="text-align: justify;"><strong>Sound by Dynaudio</strong></p>
# <p style="text-align: justify;">MSI worked with Dynaudio, world-class name in sound system design from Denmark, studying electrical circuits, dozens of speaker drivers, and how to best arrange internal parts and components to optimize sound. For over a year, they tweaked the sound and developed electrical circuits and materials with the best sound response. The results of their studies have been incorporated into MSI's high-end GT Series gaming NBs--the laptops with the best stereo sound in the industry. The GT Series, the only laptops in the industry with a Dynaudio sound system, clearly leads the industry not simply in terms of volume, but also in terms of stereo and crisp, clear sound for a more enjoyable gaming and multimedia experience.</p>
# <p style="text-align: justify;"><strong>Exclusive Audio Boost enhanced 30% more clear sound and fidelity detail for external headsets and speakers</strong></p>
# <p style="text-align: justify;">The MSI Audio Boost design enhances the output sound detail and sound stage by 30% more. The gold flash audio jack provides stable sound transmission (reduced obstruction) and works in conjunction with the optimized headsets AMP (Audio Power Amplifier) design, characterized by low noise and low distortion, to greatly enhance headphone performance and faithfully reproduce each acoustic detail.</p>
# <p style="text-align: justify;"><strong>Automatically apply more power to boost CPU and graphics performance!</strong></p>
# <p style="text-align: justify;">"NOS is the MSI unique feature to use Hybrid Power design, combined with CPU Boost from Intel, GPU Boost from NVIDIA graphics and Cooler Boost 2 from MSI special design, this feature brings out more than 10% performance enhancements.</p>
# <p style="text-align: justify;">On MSI GT-series Gaming notebooks, when the system total usage power is over the maxima limitation of 180W adaptor supply, NOS will automatically turn on to apply more currents and watts to support GPU and to keep the boost work. It lets user get 10% more benefits on benchmarks an gaming performance."</p>
# 						    </div>
# </div>'''
#
# link = re.compile(r"(<\w+.*?)(style|class)\s*?=\s*?['|\"].*?['|\"](.*?>)")
# print  re.sub(link,r'\1\3',html)
# exit()
#
# print re.sub( re.compile(r"<[^(p|div|/p|/div)]\s*?.*?>",re.I),'', html)
# exit()
class parser_attrs:
    attrs = []
    xml = ''

    def xml(self, xml):
        self.xml = xml
        return self
    def rm(self, attr):
        self.attrs.append(attr)
        return self

    def __rm(self):
        attrs = ''
        for attr in self.attrs:
            attrs = attrs + '|' +attr
        attrs = attrs.strip('|')
        print self.attrs
        if attrs:
            print r"(<\w+.*?)("+attrs+")\s*?=\s*?['|\"].*?['|\"](.*?>)"
            link = re.compile(r"(<\w+.*?)("+attrs+")\s*?=\s*?['|\"].*?['|\"](.*?>)")
            self.xml = re.sub(link,r'\1\3',self.xml)

    def run(self):
        self.__rm()
        return self.xml

class parser_tags:
    allow_tags = []
    del_tags = []
    isEmpty = False
    xml = ''

    def xml(self, xml):
        self.xml = xml
        return self

    def rm(self, tag):
        self.del_tags.append(tag)
        return self

    def kp(self, tag):
        self.allow_tags.append(tag)
        return self

    def empty(self):
        self.isEmpty = True
        return  self

    def __rm(self):
        tags = ''
        for tag in self.del_tags:
            tags = tags+'|'+tag
        tags = tags.strip('|')

        if tags:
            link = re.compile(r"</?("+tags+").*?>", re.I)
            self.xml = re.sub( link, '', self.xml)

    def __kp(self):
        tags = ''
        for tag in self.allow_tags:
            tags = tags + '|' + tag + '|/' + tag
        tags = tags.strip('|')

        if tags:
            link = re.compile(r"<[^("+tags+")].*?>",re.I)
            self.xml = re.sub(link,'',self.xml)

    def __empty(self):
        if self.isEmpty:
            link = re.compile(r"\s+")
            self.xml = re.sub(link,' ', self.xml)

    def run(self):
        self.__rm()
        self.__kp()
        self.__empty()
        return self.xml

class parser:
    hs = url = base_url = db = ''
    def __init__(self):
        self.db = DB()

    def get_field_value(self, value, value_type=None):
        if value_type == 'img':
            return self.get_img_url(value)

        return value

    def get_all_url(self,website_id):
        res = self.db.execute('SELECT url FROM le_goods WHERE website_id=%s AND isshow=1',[website_id])
        return res.fetchall()

    def get_img_url(self, url):
        return urlparse.urljoin(self.base_url, url)

    def set_defalut(self, spider=None, response=None, text=None):
        if text!=None:
            self.hs = Selector(text=text)
            self.url = 'http://www.ilovedeals.sg'
            self.base_url = 'http://www.ilovedeals.sg'
        else:
            self.hs = Selector(response)
            self.url = response.url
            self.base_url = get_base_url(response)

        if spider == None:
            item = SgGoodsItem()
        else:
            item = eval(spider.xpath_item+'()')

        for name,value in vars(SgGoodsItem).items():
            if name == 'fields':
                for i in value:
                    if i== 'image_urls' or i == 'images':
                        item[i] = []
                    else:
                        item[i] = ''
        return item

    def run(self, spider=None, response=None, xml=None, text=None):
        return self.set_defalut(spider=spider, response=response, text=text)

    def xpath(self):
        pass

    def reg(self):
        pass

class sg_parser(parser):

    def run(self, spider=None, response=None, xml=None, text=None):

        item = self.set_defalut(spider=spider, response=response, text=text)
        url = self.url

        # is follow
        follow = xml.xpath("//targets//follow/parser/@xpath").extract()
        if follow:
            url_id = self.hs.xpath(follow[0]).extract()
            if url_id:
                id = url_id[0].strip()
                #item['name'] = hashlib.sha1(id).hexdigest()
            else:
                item['name'] = False
                return item
        # is has
        website_id = xml.xpath("//site/@website_id").extract()
        exist_name = xml.xpath("//targets//exist/@name").extract()
        if website_id:
            website_id = website_id[0]

        exist_value = ''
        if exist_name:
            exist_name = exist_name[0]
            exist_val = xml.xpath("//targets//exist/parser/@xpath").extract()
            if exist_val:
                exist_value = self.hs.xpath(exist_val[0]).extract()
                if exist_value:
                    exist_value = exist_value[0]
            else:
                exist_val = xml.xpath("//targets//exist/parser/@val").extract()
                if exist_val:
                    exist_value = exist_val[0]
                    try:
                        exist_value = eval(exist_value)
                    except:
                        logs(time.strftime("------%Y-%m-%d %H:%M:%S-")  +exist_value +' eval error.')
                        exit(0)
            rep_val = xml.xpath("//targets//exist/parser/@rep").extract()
            if len( rep_val ) > 0:
                rep_val = rep_val[0]
                reg_value = xml.xpath("//targets//exist/parser/@value").extract()
                if reg_value:
                    reg_value = self.get_field_value(reg_value[0], 'str')
                    exist_value = exist_value.replace(rep_val, reg_value)
                else:
                    logs(time.strftime("------%Y-%m-%d %H:%M:%S") +' '+ rep_val + ' Field rep No Define Value.')
                    exit(0)

            if exist_value:
                pass
            else:
                logs(time.strftime("------%Y-%m-%d %H:%M:%S")  +' '+ exist_name + ' No Exist value.')
                exit(0)
        else:
            logs(time.strftime("------%Y-%m-%d %H:%M:%S") +' No Exist name.')
            exit(0)
        res = self.db.execute("SELECT goods_id, name, price, original_price,isshow FROM le_goods WHERE website_id=%s AND "+exist_name+"=%s", [website_id,exist_value])
        #print ("SELECT goods_id, name, price, original_price FROM le_goods WHERE website_id=%s AND "+exist_name+"=%s") % (website_id,exist_value)
        row = res.fetchone()
        if row != None:
            item['goods'] = row

        fields = xml.xpath("//targets//model//field").extract()
        for field in fields:
            fsl = Selector(text=field, type='xml')
            name = fsl.xpath("//field/@name").extract()
            define = fsl.xpath("//field/@def").extract()
            isArray = fsl.xpath("//field/@isArray").extract()
            filed_type = fsl.xpath("//field/@type").extract()

            if len(filed_type) > 0:
                filed_type = filed_type[0]
            else:
                filed_type = ''

            if len(name) < 1 :
                logs(time.strftime("------%Y-%m-%d %H:%M:%S") + ' Field Name No Define.')
                exit(0)
            _this = ''
            name = name[0].strip()
            if define:
                if item[name]:
                    _this = item[name]
                    pass
                else:
                    item[name] = define[0].strip()
                    _this = define[0].strip()

            if isArray:
                item[name] = []
                _this = []

            xpath_list = fsl.xpath("//parsers/parser").extract()
            _Tags = parser_tags()
            _Attrs = parser_attrs()

            for xpath in xpath_list:
                xsl = Selector(text=xpath, type='xml')
                xpath = xsl.xpath("//parser/@xpath").extract()
                if len( xpath ) > 0:
                    for xp in xpath:
                        val = self.hs.xpath(xp).extract()
                        if isArray:
                            for v in val:
                                _this.append( self.get_field_value(v.strip(), filed_type))
                        else:
                            if len(val) > 0:
                                _this = self.get_field_value(val[0].strip(), filed_type)

                rep = xsl.xpath("//parser/@rep").extract()

                # rep
                if len( rep ) > 0:
                    # if name=='ExpiryTime':
                    #     print rep[0],'--',int(time.time())
                    _this = eval(rep[0])

                # grep
                grep = xsl.xpath('//parse/@grep').extract()
                if grep:
                    _this = eval(grep[0])

            item[name] = _this

            ''''''''''''''''''''''''''''''''''''''''''''''''''

            item['url'] = self.url
            if item['ExpiryTime']:
                item['ExpiryTime'] = int(item['ExpiryTime'])
            #else:
             #item['ExpiryTime'] = int(time.time()) + 864000

            if row == None and item['oldImg']:
                item['image_urls'] = item['oldImg']

            # if row != None and item['oldImg'] and row['img'] == '':
            #     item['image_urls'] = item['oldImg']

            # if len(item['image_urls']) < 1 :
            #     item['image_urls'] = ['http://www.ilovedeals.sg/images/ilovedeals-logo.png']
        return item
