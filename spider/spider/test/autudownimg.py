#!/usr/bin/python
#coding=utf-8
import time
import sys,os,glob
import re
import time
from PIL import Image
from download import *



sys.path.append( '/wwwroot/spiderling/spider')
from spider.tools.db import *
from spider.tools.SimpleClassifier import *

reload(sys)

download_path = '/wwwroot/dir/uploaded/'


#循环下载列表固定的  ---就是wallpaper,enterdesk等网站
def file_path( url):
        #image_guid = request.url.split('/')[-1]
        image_guid = hashlib.sha1(url).hexdigest()
        path = image_guid[0:2]
        return '%s/%s/original/%s.jpg' % (time.strftime("%Y"),time.strftime("%m%d"), image_guid)

# 缩略图路径
def thumb_path( url,thumb_id):
    image_guid = hashlib.sha1(url).hexdigest()
    path = image_guid[0:2] #thumbs
    #return 'full/%s%s.jpg' % (path, image_guid)
    #thumb_guid = hashlib.sha1(request.url).hexdigest()  # change to request.url after deprecation
    return '%s/%s/%s/%s.jpg' % (time.strftime("%Y"),time.strftime("%m%d"),thumb_id,image_guid)


if __name__ == "__main__":

    splider=BrowserBase()
    #print time.strftime("%Y-%m-%d", 1428857999)
    date_str = str(int(time.time() - 432000))
    ''''''''''''''''''''''''''''''''''''''''''''''''''''
   sg处理
    '''''''''''''''''''''''''''''''''''''''''''''''''''

    db_link = 'sg'
    db = DB(db_link)
    #scf = SimpleClassifier(db_link)
    new_download_path = download_path+db_link+'/'
    #res = db.execute('SELECT goods_id, name,cate_id,oldimg FROM le_goods WHERE website_id in(12) and img ="" and length(oldimg)>0')
    res = db.execute('SELECT goods_id, name,cate_id,oldimg FROM le_goods WHERE  img ="" and length(oldimg)>0 and addtime>'+ date_str)

    goods_list = res.fetchall()
    for goods in goods_list:
        # if goods:
        #     print goods
        #     oldimg = goods['oldimg'].split('|')
        #     oldimg = oldimg[0]
        #     print oldimg
        #     continue;
        # if True:
        #     goods = {}
        #     goods['goods_id'] = 2
        #     goods['oldimg'] = 'http://www.juztoday.com/deal/3120/img/header2.jpg'
        oldimg = goods['oldimg'].split('|')
        oldimg = oldimg[0]
        full_path = new_download_path + file_path(oldimg)
        thumb_100 = new_download_path + thumb_path(oldimg,'thumb100')
        thumb_250 = new_download_path + thumb_path(oldimg,'thumb250')
        thumb_400 = new_download_path + thumb_path(oldimg,'thumb400')
        thumb_100_size = 100,100
        thumb_250_size = 250,250
        thumb_400_size = 400,300
        #os.path.abspath(
        if False ==os.path.exists(os.path.dirname(full_path)):
            os.makedirs(os.path.dirname(full_path))
        if False ==os.path.exists(os.path.dirname(thumb_100)):
            os.makedirs(os.path.dirname(thumb_100))
        if False ==os.path.exists(os.path.dirname(thumb_250)):
            os.makedirs(os.path.dirname(thumb_250))
        if False ==os.path.exists(os.path.dirname(thumb_400)):
            os.makedirs(os.path.dirname(thumb_400))

        splider.save(oldimg,full_path)
        if os.path.exists(full_path):

            try:
                im=Image.open(full_path)


                w,h=im.size
                im.thumbnail(thumb_100_size,Image.ANTIALIAS)
                #im_s.show()
                im.save(thumb_100)
                print thumb_100

                im=Image.open(full_path)
                w,h=im.size
                im.thumbnail(thumb_250_size,Image.ANTIALIAS)
                #im_s.show()
                im.save(thumb_250)
                print thumb_250

                im=Image.open(full_path)
                w,h=im.size
                im.thumbnail(thumb_400_size,Image.ANTIALIAS)
                #im_s.show()
                im.save(thumb_400)
                print thumb_400

                img = '/uploaded/'+thumb_400.replace(new_download_path,'')

                small_pic =  '/uploaded/'+thumb_100.replace(new_download_path,'')
                big_pic =  '/uploaded/'+full_path.replace(new_download_path,'')

                res = db.execute("UPDATE le_goods SET isshow=1,`img`=%s, `deal_img`=%s, `small_pic`=%s,`bigpic`=%s,taoke_url='1' WHERE goods_id = %s ",[img,img,small_pic,big_pic,goods['goods_id']])
                print res._last_executed
            except Exception, e:
                continue

    ''''''''''''''''''''''''''''''''''''''''''''''''''''
    my处理
    '''''''''''''''''''''''''''''''''''''''''''''''''''
    db_link = 'my'
    db = DB(db_link)
    #scf = SimpleClassifier(db_link)
    new_download_path = download_path+db_link+'/'
    #res = db.execute('SELECT goods_id, name,cate_id,oldimg FROM le_goods WHERE website_id in(12) and img ="" and length(oldimg)>0')
    res = db.execute('SELECT goods_id, name,cate_id,oldimg FROM le_goods WHERE  img ="" and length(oldimg)>0 and addtime>'+date_str)

    goods_list = res.fetchall()

    for goods in goods_list:
        # if goods:
        #     print goods
        #     print goods['oldimg'].split('|')
        #     continue;
        # if True:
        #     goods = {}
        #     goods['goods_id'] = 2
        #     goods['oldimg'] = 'http://static2.ensogo.com.my/assets/deals/2ef7cd05c5074ba250163c1c5bfbd9bd/main_deal.jpg?ts=1430418507'
        oldimg = goods['oldimg'].split('|')
        oldimg = oldimg[0]
        full_path = new_download_path + file_path(oldimg)
        thumb_100 = new_download_path + thumb_path(oldimg,'thumb100')
        thumb_250 = new_download_path + thumb_path(oldimg,'thumb250')
        thumb_400 = new_download_path + thumb_path(oldimg,'thumb400')
        thumb_100_size = 100,100
        thumb_250_size = 250,250
        thumb_400_size = 400,300
        #os.path.abspath(
        if False ==os.path.exists(os.path.dirname(full_path)):
            os.makedirs(os.path.dirname(full_path))
        if False ==os.path.exists(os.path.dirname(thumb_100)):
            os.makedirs(os.path.dirname(thumb_100))
        if False ==os.path.exists(os.path.dirname(thumb_250)):
            os.makedirs(os.path.dirname(thumb_250))
        if False ==os.path.exists(os.path.dirname(thumb_400)):
            os.makedirs(os.path.dirname(thumb_400))

        splider.save(oldimg,full_path)
        if os.path.exists(full_path):

            try:
                im=Image.open(full_path)


                w,h=im.size
                im.thumbnail(thumb_100_size,Image.ANTIALIAS)
                #im_s.show()
                im.save(thumb_100)
                print thumb_100

                im=Image.open(full_path)
                w,h=im.size
                im.thumbnail(thumb_250_size,Image.ANTIALIAS)
                #im_s.show()
                im.save(thumb_250)
                print thumb_250

                im=Image.open(full_path)
                w,h=im.size
                im.thumbnail(thumb_400_size,Image.ANTIALIAS)
                #im_s.show()
                im.save(thumb_400)
                print thumb_400

                img = '/uploaded/'+thumb_400.replace(new_download_path,'')

                small_pic =  '/uploaded/'+thumb_100.replace(new_download_path,'')
                big_pic =  '/uploaded/'+full_path.replace(new_download_path,'')

                res = db.execute("UPDATE le_goods SET isshow=1,`img`=%s, `deal_img`=%s, `small_pic`=%s,`bigpic`=%s,taoke_url='1' WHERE goods_id = %s ",[img,img,small_pic,big_pic,goods['goods_id']])
                print res._last_executed
            except Exception, e:
                continue
    print '下载完成！'