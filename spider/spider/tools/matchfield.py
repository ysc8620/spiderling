#!/usr/bin/python
#coding=utf-8

import sys,os
reload(sys)
sys.setdefaultencoding('utf8')

from scrapy.selector import Selector
from spider.items import DealItem
from scrapy.utils.response import get_base_url
import urlparse
import time
from spider.tools.common import *
from spider.tools.db import DB

db = DB()

def match_dmoz_field(response=None, xml=None, text=None):
    if text!=None:
        hs = Selector(text=text)
        base_url = ''
        url = ''
    else:
        hs = Selector(response)
        base_url = get_base_url(response)
        url = response.url

    item = DealItem()
    for name,value in vars(DealItem).items():
        if name == 'fields':
            for i in value:
                if i== 'image_urls' or i == 'images':
                    item[i] = []
                else:
                    item[i] = ''
    # is follow
    follow = xml.xpath("//targets//follow/parser/@xpath").extract()
    if follow:
        url_id = hs.xpath(follow[0]).extract()
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
            exist_value = hs.xpath(exist_val[0]).extract()
            if exist_value:
                exist_value = exist_value[0]
        else:
            exist_val = xml.xpath("//targets//exist/parser/@val").extract()
            if exist_val:
                exist_value = exist_val[0]
                try:
                    print '=============+'+exist_value+'+================================='
                    exist_value = eval(exist_value)
                except:
                    logs(time.strftime("------%Y-%m-%d %H:%M:%S-")  +exist_value +' eval error.')
                    exit(0)

        if exist_value:
            pass
        else:
            logs(time.strftime("------%Y-%m-%d %H:%M:%S")  +' '+ exist_name + ' No Exist value.')
            exit(0)
    else:
        logs(time.strftime("------%Y-%m-%d %H:%M:%S") +' No Exist name.')
        exit(0)
    res = db.execute("SELECT goods_id, name, price, original_price FROM le_goods WHERE website_id=%s AND "+exist_name+"=%s", [website_id,exist_value])
    # print ("SELECT goods_id, name, price, original_price FROM le_goods WHERE website_id=%s AND "+exist_name+"=%s") % (website_id,exist_value)
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

        name = name[0].strip()
        if define:
            item[name] = define[0].strip()

        if isArray:
            item[name] = []

        xpath_list = fsl.xpath("//parsers/parser").extract()
        for xpath in xpath_list:
            xsl = Selector(text=xpath, type='xml')
            xpath = xsl.xpath("//parser/@xpath").extract()
            if len( xpath ) > 0:
                for xp in xpath:
                    val = hs.xpath(xp).extract()
                    if isArray:
                        for v in val:
                            item[name].append(v.strip())
                    else:
                        if val:
                            item[name] = val[0].strip()

            rep = xsl.xpath("//parser/@rep").extract()
            if len( rep ) > 0:
                rep = rep[0]
                value = xsl.xpath("//parser/@value").extract()
                if value:
                    value = value[0]
                else:
                    logs(time.strftime("------%Y-%m-%d %H:%M:%S") +' '+ name + ' Field rep No Define Value.')
                    exit(0)
                if isArray:
                    for i,row in item[name]:
                        item[name][i] = row.replace(rep, value)
                else:
                    item[name] = item[name].replace(rep, value)
        ''''''''''''''''''''''''''''''''''''''''''''''''''

        item['url'] = url
        item['ExpiryTime'] = int(time.time()) + 864000

        if row == None and item['oldImg']:
            item['image_urls'] = item['oldImg']

        # if len(item['image_urls']) < 1 :
        #     item['image_urls'] = ['http://www.ilovedeals.sg/images/ilovedeals-logo.png']
    return item
