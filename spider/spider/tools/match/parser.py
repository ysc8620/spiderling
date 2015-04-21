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

    def xml(self, xml=''):
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
    hs = url = base_url = db = link_db = ''
    def __init__(self, db=None):
        self.link_db = db
        print '-------------------'
        print self.link_db
        print '-------------------'
        self.db = DB(self.link_db)

    def get_field_value(self, value, value_type=None):
        if value_type == 'img':
            return self.get_img_url(value)
        return value

    def get_all_url(self,website_id):
        print '-------++++++++'
        print self.db
        print website_id
        print '--------++++++++'

        res = self.db.execute('SELECT url FROM le_goods WHERE website_id=%s AND isshow=1',[website_id])
        return res.fetchall()

    def get_img_url(self, url):
        return urlparse.urljoin(self.base_url, url)

    def set_defalut(self, spider=None, response=None, text=None):
        if text!=None:
            self.hs = Selector(text=text)
            self.url = ''
            self.base_url = ''
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

    def run(self, spider=None, response=None, xml=None, text=None):
        return self.set_defalut(spider=spider, response=response, text=text)

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

    def run(self, spider=None, response=None, xml=None, text=None):
        jsonData = json.loads(response.body_as_unicode().strip().encode('utf8'))
        for jfield in jsonData['deals']:
            item = self.set_defalut(spider=spider, response=response, text=text)
            # is has
            website_id = xml.xpath("//site/@website_id").extract()
            if website_id:
                website_id = website_id[0]

            exist_name = xml.xpath("//targets//exist/@name").extract()
            exist_value = ''
            if exist_name:
                exist_name = exist_name[0].strip()
                exist_list = xml.xpath("//targets//exist/parser")
                for exist in exist_list:
                    xpath = exist.xpath('@xpath').extract()
                    if xpath:
                        exist_val = self.hs.xpath(xpath[0]).extract()
                        if exist_val:
                            exist_value = exist_val[0]
                        continue
                    val = exist.xpath('@val').extract()
                    if val:
                        try:
                            exist_value = eval(val[0])
                        except Exception, e:
                            logs(time.strftime("------%Y-%m-%d %H:%M:%S-")  +val[0] +' eval error.')
                            exit(0)
                        continue
                res = self.db.execute("SELECT goods_id, name, price, original_price,isshow FROM le_goods WHERE website_id=%s AND "+exist_name+"=%s", [website_id,exist_value])
                row = res.fetchone()
                if row != None:
                    item['goods'] = row

            fields = xml.xpath("//targets//model//field")
            for field in fields:
                name = field.xpath("@name").extract()
                define = field.xpath("@def").extract()
                isArray = field.xpath("@isArray").extract()

                if len(name) < 1 :
                    logs(time.strftime("------%Y-%m-%d %H:%M:%S") + ' Field Name No Define.')
                    exit(0)
                _this = ''
                name = name[0].strip()
                if define:
                    if item[name]:
                        _this = item[name]
                    else:
                        item[name] = define[0].strip()
                        _this = define[0].strip()

                if isArray:
                    item[name] = []
                    _this = []

                field_html = field.extract()
                if field_html:
                    field_xml = Selector(text=field_html,type='xml')
                    parser_list = field_xml.xpath("//parsers/parser")
                    #print parser_list
                    for parser in parser_list:
                        _Tags = parser_tags(self)
                        _Attrs = parser_attrs(self)
                        _Spread = parser_spread(self)
                        rep = parser.xpath("@val").extract()
                        # rep
                        if len( rep ) > 0:
                            try:
                                _this = eval(rep[0])
                            except:
                                logs(time.strftime("------%Y-%m-%d %H:%M:%S") + rep[0]+ ' rep eval error.')
                            continue

                item[name] = _this

                ''''''''''''''''''''''''''''''''''''''''''''''''''

            #item['url'] = self.url
            if row == None and item['oldImg']:
                item['image_urls'] = item['oldImg']

            yield item
        #return item

    def getExpiryTime(times):
        return (int(time.time())-10) if (times < 0) else (int(time.time())+864000)

class sg_parser(parser):

    def run(self, spider=None, response=None, xml=None, text=None):

        item = self.set_defalut(spider=spider, response=response, text=text)
        url = self.url

        # is follow
        follows = xml.xpath("//targets//follow/parser")
        if follows:
            for follow in follows:
                xpath = follow.xpath('@xpath').extract()
                if xpath:
                    url_id = self.hs.xpath(xpath[0]).extract()
                    if url_id:
                        id = url_id[0].strip()
                    else:
                        item['name'] = False
                        return item
                    continue

                val = follow.xpath('@val').extract()
                if val:
                    try:
                        url_id = eval(val[0])
                    except Exception,e:
                        pass
                    if url_id:
                        id = url_id[0].strip()
                    else:
                        item['name'] = False
                        return item
                    continue

        # is has
        website_id = xml.xpath("//site/@website_id").extract()
        if website_id:
            website_id = website_id[0].strip()

        exist_name = xml.xpath("//targets//exist/@name").extract()
        exist_value = ''
        if exist_name:
            exist_name = exist_name[0].strip()
            exist_list = xml.xpath("//targets//exist/parser")

            for exist in exist_list:
                xpath = exist.xpath('@xpath').extract()
                if xpath:
                    exist_val = self.hs.xpath(xpath[0]).extract()
                    if exist_val:
                        exist_value = exist_val[0]
                    continue
                val = exist.xpath('@val').extract()
                if val:
                    try:
                        exist_value = eval(val[0])
                    except Exception, e:
                        logs(time.strftime("------%Y-%m-%d %H:%M:%S-")  +val[0] +' eval error.')
                        exit(0)
                    continue
            res = self.db.execute("SELECT goods_id, name, price, original_price,isshow FROM le_goods WHERE website_id=%s AND "+exist_name+"=%s", [website_id,exist_value])
            row = res.fetchone()
            if row != None:
                item['goods'] = row

        fields = xml.xpath("//targets//model//field")
        for field in fields:
            name = field.xpath("@name").extract()
            define = field.xpath("@def").extract()
            isArray = field.xpath("@isArray").extract()
            filed_type = field.xpath("@type").extract()

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
                else:
                    item[name] = define[0].strip()
                    _this = define[0].strip()

            if isArray:
                item[name] = []
                _this = []
            #field_xml = Selector(text=field.extract()[0])
            field_html = field.extract()
            if field_html:
                field_xml = Selector(text=field_html,type='xml')
                parser_list = field_xml.xpath("//parsers/parser")
                #print parser_list
                for parser in parser_list:
                    _Tags = parser_tags(self)
                    _Attrs = parser_attrs(self)
                    _Spread = parser_spread(self)

                    xpath = parser.xpath("@xpath").extract()
                    if len( xpath ) > 0:
                        re= parser.xpath("@re").extract()
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

                        continue

                    rep = parser.xpath("@rep").extract()
                    if len( rep ) > 0:
                        try:
                            _this = eval(rep[0])
                        except Exception, e:
                            logs(time.strftime("------%Y-%m-%d %H:%M:%S") + rep[0]+ ' rep eval error.' + e.message)

                item[name] = _this

        item['url'] = self.url
        if item['ExpiryTime']:
            item['ExpiryTime'] = int(item['ExpiryTime'])

        if row == None and item['oldImg']:
            item['image_urls'] = item['oldImg']
        return item
