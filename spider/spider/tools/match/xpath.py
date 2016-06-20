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
from spider.tools.common import *

def get_field_value(val, type):
    # if type == 'int':
    #     return int(val)
    #
    # if type == 'float':
    #     return float(val)

    return val

class xpath_base:
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

class sg_xpath(xpath_base):

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
                    reg_value = get_field_value(reg_value[0], 'str')
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

            name = name[0].strip()
            if define:
                if item[name]:
                    pass
                else:
                    item[name] = define[0].strip()

            if isArray:
                item[name] = []

            xpath_list = fsl.xpath("//parsers/parser").extract()
            for xpath in xpath_list:
                xsl = Selector(text=xpath, type='xml')
                xpath = xsl.xpath("//parser/@xpath").extract()
                if len( xpath ) > 0:
                    for xp in xpath:
                        val = self.hs.xpath(xp).extract()
                        if isArray:
                            for v in val:
                                if name == 'oldImg':
                                    if v.strip().index('http') > -1:
                                        print '-------------------------------------------------'
                                        item[name].append( self.get_field_value(v.strip(), filed_type))
                                    else:
                                        print '++++++++++++++++++++++++++++++++++++++++++'
                                        item[name].append( self.get_field_value(urlparse.urljoin(self.base_url, v.strip()), filed_type))
                                else:
                                    item[name].append( self.get_field_value(v.strip(), filed_type))
                                    print '======================================================'
                                    #
                        else:
                            print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
                            if len(val) > 0:
                                item[name] = self.get_field_value(val[0].strip(), filed_type)

                rep = xsl.xpath("//parser/@rep").extract()
                if len( rep ) > 0:
                    rep = rep[0]
                    value = xsl.xpath("//parser/@value").extract()
                    if value:
                        value = self.get_field_value(value[0], filed_type)
                    else:
                        logs(time.strftime("------%Y-%m-%d %H:%M:%S") +' '+ name + ' Field rep No Define Value.')
                        exit(0)

                    if isArray:
                        for i,row in item[name]:
                            item[name][i] = row.replace(rep, value)
                    else:
                        if item[name]:
                            item[name] = item[name].replace(rep, value)
            ''''''''''''''''''''''''''''''''''''''''''''''''''

            item['url'] = self.url
            if item['ExpiryTime']:
                item['ExpiryTime'] = int(time.time())+int(item['ExpiryTime'])
            else:
                item['ExpiryTime'] = int(time.time()) + 864000

            if row == None and item['oldImg']:
                item['image_urls'] = item['oldImg']

            # if row != None and item['oldImg'] and row['img'] == '':
            #     item['image_urls'] = item['oldImg']

            # if len(item['image_urls']) < 1 :
            #     item['image_urls'] = ['http://www.ilovedeals.sg/images/ilovedeals-logo.png']

        return item
