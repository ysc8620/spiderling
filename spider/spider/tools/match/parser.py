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
import json

# 特殊扩展类处理特例
class parser_spread():
    parser = None

    def __init__(self, parser=None):
        self.parser = parser

    def omigo_json_img(self, json_html):
        js_data = json.loads(json_html)
        ret = []
        for i in js_data:
            print i['large']+'==============='
            ret.append( self.parser.get_field_value(i['large'],'img'))
        return ret

    def run(self):
        pass

class parser_attrs:
    attrs = []
    xml = ''

    parser = None
    def __init__(self, parser=None):
        self.parser = parser
        self.attrs = []
        self.xml = ''

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
        if attrs:
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
    parser = None
    def __init__(self, parser=None):
        self.parser = parser

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
    link_db = 'sg'
    def __init__(self, db=None):
        self.db = db

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
            self.link_db = spider.link_db
            self.hs = Selector(response)
            self.url = response.url
            self.base_url = get_base_url(response)

        if spider == None:
            item = SgGoodsItem()
        else:
            try:
                item = eval(spider.xpath_item+'()')
            except Exception, e:
                print spider.xpath_item + " xpath item eval error"+ e.message

        for name,value in vars(SgGoodsItem).items():
            if name == 'fields':
                for i in value:
                    if i== 'image_urls' or i == 'images':
                        item[i] = []
                    else:
                        item[i] = ''
        item['db'] = self.link_db
        return item

    def run(self, spider=None, response=None, xml=None, text=None,db=None):
        self.db = db
        return self.set_defalut(spider=spider, response=response, text=text)

    def xpath(self):
        pass

    def reg(self):
        pass

class my_ensogo(parser):
    def set_defalut(self, spider=None, response=None, text=None):
        if spider == None:
            item = SgGoodsItem()
        else:
            self.link_db = spider.link_db
            try:
                item = eval(spider.xpath_item+'()')
            except Exception, e:
                print spider.xpath_item+" xpath item eval error "+e.message

        for name,value in vars(SgGoodsItem).items():
            if name == 'fields':
                for i in value:
                    if i== 'image_urls' or i == 'images':
                        item[i] = []
                    else:
                        item[i] = ''
        item['db'] = self.link_db
        return item

    def run(self, spider=None, response=None, xml=None, text=None,db=None):
        self.db = db
        #item = self.set_defalut(spider=spider, response=response, text=text)

        jsonData = json.loads(response.body_as_unicode().strip().encode('utf8'))
        for jfield in jsonData['deals']:
            item = self.set_defalut(spider=spider, response=response, text=text)
            # is has
            website_id = xml.xpath("//site/@website_id").extract()
            exist_name = xml.xpath("//targets//exist/@name").extract()
            if website_id:
                website_id = website_id[0]

            exist_value = ''
            if exist_name:
                exist_name = exist_name[0]
                exist_val = xml.xpath("//targets//exist/parser/@val").extract()
                if exist_val:
                    exist_value = exist_val[0]
                    try:
                        exist_value = eval(exist_value)
                    except:
                        logs(time.strftime("------%Y-%m-%d %H:%M:%S-")  +exist_value +' eval error.')
                        exit(0)
            else:
                logs(time.strftime("------%Y-%m-%d %H:%M:%S") +' No Exist name.')
                exit(0)

            res = self.db.execute("SELECT goods_id, name, price, original_price,isshow FROM le_goods WHERE website_id=%s AND "+exist_name+"=%s", [website_id,exist_value])
            row = res.fetchone()
            if row != None:
                item['goods'] = row

            fields = xml.xpath("//targets//model//field").extract()
            for field in fields:
                fsl = Selector(text=field, type='xml')
                name = fsl.xpath("//field/@name").extract()
                define = fsl.xpath("//field/@def").extract()
                isArray = fsl.xpath("//field/@isArray").extract()

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
                for xpath in xpath_list:
                    xsl = Selector(text=xpath, type='xml')
                    _Tags = parser_tags(self)
                    _Attrs = parser_attrs(self)
                    _Spread = parser_spread(self)
                    rep = xsl.xpath("//parser/@val").extract()
                    # rep
                    if len( rep ) > 0:
                        try:
                            _this = eval(rep[0])
                        except:
                            print rep[0]
                            logs(time.strftime("------%Y-%m-%d %H:%M:%S") + rep[0]+ ' rep eval error.')

                item[name] = _this

                ''''''''''''''''''''''''''''''''''''''''''''''''''

            #item['url'] = self.url
            # if row == None and item['oldImg']:
            item['image_urls'] = item['oldImg']

            yield item
        #return item

    def getExpiryTime(times):
        return (int(time.time())-10) if (times < 0) else (int(time.time())+864000)

class sg_parser(parser):

    def run(self, spider=None, response=None, xml=None, text=None,db=None):
        self.db = db
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
            for xpath in xpath_list:
                xsl = Selector(text=xpath, type='xml')
                _Tags = parser_tags(self)
                _Attrs = parser_attrs(self)
                _Spread = parser_spread(self)

                xpath = xsl.xpath("//parser/@xpath").extract()
                if len( xpath ) > 0:
                    re= xsl.xpath("//parser/@re").extract()
                    for xp in xpath:
                        if re:
                            val = self.hs.xpath(xp).re(re[0])
                        else:
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
                    try:
                        _this = eval(rep[0])
                    except Exception, e:
                        logs(time.strftime("------%Y-%m-%d %H:%M:%S") + rep[0]+ ' rep eval error.' + e.message)

            item[name] = _this

            ''''''''''''''''''''''''''''''''''''''''''''''''''

            item['url'] = self.url
            if item['ExpiryTime']:
                item['ExpiryTime'] = int(item['ExpiryTime'])
            #else:
             #item['ExpiryTime'] = int(time.time()) + 864000

            # if row == None and item['oldImg']:
            item['image_urls'] = item['oldImg']

            # if row != None and item['oldImg'] and row['img'] == '':
            #     item['image_urls'] = item['oldImg']

            # if len(item['image_urls']) < 1 :
            #     item['image_urls'] = ['http://www.ilovedeals.sg/images/ilovedeals-logo.png']

        return item
