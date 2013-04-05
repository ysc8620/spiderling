# -*- coding: utf-8 -*-
__author__ = 'ShengYue'
from lxml import etree
from os.path import join, getsize
from model.curl import curl
import csv
import re
import string
import re

header = ("*:通用商品类型","bn:商品货号","ibn:规格货号","col:分类","col:品牌","col:市场价","col:成本价","col:销售价","col:商品名称",
    "col:上架","col:规格","price:普通会员","price:高级会员","price:VIP会员","col:缩略图","col:图片文件","col:商品简介",
    "col:详细介绍","col:重量","col:单位","col:库存","col:货位","col:大图片","col:小图片" )

class main:
    def init(self, url, cate):
        self.curl = curl()

        html = self.curl.read(url)
        #fop = open('./html.html')
        #print getsize('./html.html')
        #fop.write(html)
        #try:
        #    html = fop.read(getsize('./html.html'))
        #    #html =  self.curl.mdcode(html)
        #finally:
        #    fop.close()
        #print html
        data = {}

        xtree = etree.HTML(html)

        # 标题
        title = xtree.xpath('//h1')
        data['name'] = string.strip(title[0].text)

        #价格
        price = xtree.xpath('//span[@id="ECS_SHOPPRICE"]')
        data['price'] = string.strip(price[0].text)

        #原价
        oldprice = xtree.xpath('//span[@class="xline"]')
        oldprice = re.findall(re.compile('[\d.]*'), string.strip(oldprice[0].text))
        data['oldprice'] = oldprice[1]


        #品牌
        #brand = xtree.xpath('//*[@id="ECS_FORMBUY"]/div/div[3]/span[2]/a')
        #data['brand'] = string.strip(brand[0].text)

        #货号
        huohao = xtree.xpath('//*[@id="ECS_FORMBUY"]/div/p/span[2]')
        data['ibn'] = string.strip(huohao[0].text)

        #大图片
        bimg = xtree.xpath('//*[@id="thumg"]')

        imgurl = string.strip(bimg[0].get('src'))
        data['bimg'] = self.curl.down(imgurl)

        #大图片
        data['simg'] = data['bimg']

        #详细
        dest = xtree.xpath('//div[@class="deszone"]/div[@class="zones"]')
        des = etree.tostring(dest[0], encoding='utf-8')
        #data['des'] = des
        reg = re.compile('\s',re.I)
        s = reg.subn(' ', des)
        data['des'] = s[0]
        data['des'] = data['des'].replace( 'src2','src')

        #print data['des']
        #下载所有图片
        #ireg = re.compile("<img\b[^<>]*?\bsrc[2\s\t\r\n]*=[\s\t\r\n]*['\"]?[\s\t\r\n]*(\?<imgUrl>[^\s\t\r\n'\"<>]*)[^<>]*?/?[\s\t\r\n]*>")
        imgreg = re.compile(r"<img\b[^<>]*?\bsrc[2\s\t\r\n]*=[\s\t\r\n]*['\"]?[\s\t\r\n]*([^\s\t\r\n'\"<>]*)[^<>]*?/?[\s\t\r\n]*>")

        ilist = imgreg.findall(data['des'])
        for img in ilist:
            try:
                print u'下载'+img
                new = self.curl.down(img)
                data['des'] = data['des'].replace( img,new)
            except:
                print u'下载失败'+img

        header = ("*:通用商品类型","bn:商品货号","ibn:规格货号","col:分类","col:品牌","col:市场价","col:成本价","col:销售价","col:商品名称",
                  "col:上架","col:规格","price:普通会员","price:高级会员","price:VIP会员","col:缩略图","col:图片文件","col:商品简介",
                  "col:详细介绍","col:重量","col:单位","col:库存","col:货位","col:大图片","col:小图片")
        #print cate
        #cate = ''
        # 拼字段
        row = (self.curl.mdcode('通用商品类型'), self.curl.mdcode(data['ibn']),'',self.curl.mdcode(cate),'',self.curl.mdcode(data['oldprice']),self.curl.mdcode(data['price']),self.curl.mdcode(data['price']),self.curl.mdcode(data['name']),'Y','',self.curl.mdcode(data['price']),self.curl.mdcode(data['price']),self.curl.mdcode(data['price']),self.curl.mdcode(data['simg']),self.curl.mdcode(data['bimg']),'',self.curl.mdcode(data['des']),'0.000','','','',self.curl.mdcode(data['bimg']),self.curl.mdcode(data['simg']))
        fop = open('tmp.csv','w+')
        writer = csv.writer(fop)
        writer.writerow(header)
        writer.writerow(row)
        print u'完成'
        fop.close()
        return True

#mai = main()
#mai.init()
#curls = curl()
#curls.down('http://www.msex.com/static/upload/1303121657296625.jpg',{})