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

def parse_groupon_oldImgl(html=''):
    if html == '':
        return []

    hs = Selector(text=html, type='html')
    data = hs.xpath("//img/@src").extract()
    return data

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
        self.db = DB(self.link_db)

    def get_field_value(self, value, value_type=None):
        if value_type == 'img':
            return self.get_img_url(value)
        return value


    def get_goods_info(self, arg):
        pass

    def get_all_url(self,website_id):
        return False
        #res = self.db.execute('SELECT url FROM le_goods WHERE website_id=%s AND isshow=1',[website_id])
        #return res.fetchall()

    def get_img_url(self, url):
        return urlparse.urljoin(self.base_url, url)

    def set_defalut(self, spider=None, response=None, text=None, type='html'):
        if text!=None:
            self.hs = Selector(text=text,type=type)
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

    def parser_item(self, html_parser, item,url,xml):
        # is follow
        follows = xml.xpath("//targets//follow/parser")
        if follows:
            for follow in follows:
                xpath = follow.xpath('@xpath').extract()
                if xpath:
                    url_id = html_parser.xpath(xpath[0]).extract()
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
        # hide //preorder-now
        val = html_parser.xpath("//a[@id='preorder-now']/div/text()").extract()
        if val:
            if val[0] == 'PRE-ORDER':
                item['name'] = False
                return item

        # is has
        website_id = xml.xpath("//site/@website_id").extract()
        if website_id:
            website_id = website_id[0].strip()

        exist_name = xml.xpath("//targets//exist/@name").extract()
        exist_value = ''
        row = None
        if exist_name:
            exist_name = exist_name[0].strip()
            exist_list = xml.xpath("//targets//exist/parser")

            for exist in exist_list:
                xpath = exist.xpath('@xpath').extract()
                if xpath:
                    exist_val = html_parser.xpath(xpath[0]).extract()
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
            res = self.db.execute("SELECT goods_id, name, price, original_price,isshow,cate_id FROM le_goods WHERE website_id=%s AND "+exist_name+"=%s", [website_id,exist_value])
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
                if len(item[name]) < 1:
                    item[name] = []
                    _this = []
                else:
                    _this = item[name]
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
                                val = html_parser.xpath(xp).re(re[0])
                            else:
                                val = html_parser.xpath(xp).extract()

                            if isArray:
                                for v in val:
                                    #_this.append( self.get_field_value(v.strip(), filed_type))

                                    if name == 'oldImg':
                                        if v.strip().find('http') > -1:
                                            _this.append( self.get_field_value(v.strip(), filed_type))
                                        else:
                                            _this.append( self.get_field_value(urlparse.urljoin(self.base_url, v.strip()), filed_type))
                                    else:
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
                if _this:
                    item[name] = _this
                else:
                    print _this,'---',name

        if item['url'] == '':
            item['url'] = self.url

        if item['ExpiryTime']:
            item['ExpiryTime'] = int(item['ExpiryTime'])

        if row == None and item['oldImg']:
            item['image_urls'] = item['oldImg']

        afterParser = xml.xpath("//afterParser/field")

        if afterParser:
            for field in afterParser:
                parser_list = field.xpath("parsers/parser/@rep").extract()
                name = field.xpath('@name').extract()
                try:
                    name = name[0]
                    for parser in parser_list:
                        data = eval(parser)
                        item[name] = data
                except Exception, e:
                    #logs(time.strftime("------%Y-%m-%d %H:%M:%S")+name+'=' +' afterParser rep eval error.' + e.message)
                    print e.message
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
            row = None
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
                res = self.db.execute("SELECT goods_id, name, price, original_price,isshow,cate_id FROM le_goods WHERE website_id=%s AND "+exist_name+"=%s", [website_id,exist_value])
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

                        rep = parser.xpath("@rep").extract()
                        if len( rep ) > 0:
                            try:
                                _this = eval(rep[0])
                            except Exception, e:
                                logs(time.strftime("------%Y-%m-%d %H:%M:%S") + rep[0]+ ' rep eval error.' + e.message)

                            continue
                #if _this
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
        model_list = xml.xpath("//targets//model")
        for model in model_list:
            model_xpath = model.xpath("@xpath").extract()
            model_is_array = model.xpath("@xpath").extract()
            if model_is_array:
                if model_xpath:
                    parser_htmls = self.hs.xpath(model_xpath[0])
                    if parser_htmls:
                        for parser_html in parser_htmls:
                            item = self.set_defalut(spider=spider, response=response, text=text)
                            #print parser_html
                            yield self.parser_item(html_parser=parser_html,item=item,url=self.url,xml=xml)
            else:
                item = self.set_defalut(spider=spider, response=response, text=text)
                yield self.parser_item(html_parser=self.hs,item=item,url=self.url,xml=xml)

class xml_parser(parser):
    def run(self, spider=None, response=None, xml=None, text=None):
        model_list = xml.xpath("//targets//model")

        for model in model_list:
            model_xpath = model.xpath("@xpath").extract()
            model_is_array = model.xpath("@is_array").extract()

            if model_is_array:
                if model_xpath:
                    item = self.set_defalut(spider=spider, response=response, text=text,type='xml')
                    parser_htmls = self.hs.xpath(model_xpath[0]).extract()
                    if parser_htmls:
                        for parser_html in parser_htmls:
                            ph = Selector(text=parser_html,type='xml')
                            item = self.set_defalut(spider=spider, response=response, text=parser_html)
                            yield self.parser_item(html_parser=ph,item=item,url=self.url,xml=xml)
            else:
                item = self.set_defalut(spider=spider, response=response, text=text)
                yield self.parser_item(html_parser=self.hs,item=item,url=self.url,xml=xml)


class test_parser(parser):
    def run(self, spider=None, response=None, xml=None, text=None):
        model_list = xml.xpath("//targets//model")
        for model in model_list:
            model_xpath = model.xpath("@xpath").extract()
            model_is_array = model.xpath("@is_array").extract()
            if model_is_array:
                if model_xpath:
                    parser_htmls = self.hs.xpath(model_xpath[0])

                    if parser_htmls:
                        for parser_html in parser_htmls:
                            item = self.set_defalut(spider=spider, response=response, text=text)
                            return self.parser_item(html_parser=parser_html,item=item,url=self.url,xml=xml)
            else:
                item = self.set_defalut(spider=spider, response=response, text=text)
                return self.parser_item(html_parser=self.hs,item=item,url=self.url,xml=xml)