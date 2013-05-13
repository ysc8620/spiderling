# -*- coding: utf-8 -*-
__author__ = 'ShengYue'
import MySQLdb
import hashlib
from log import *

db_host = '127.0.0.1'
db_name = 'root'
db_passwd = 'LEsc2008'
db_dbname = 'python'
db_port = 3306

'''
链接管理
'''
class linkdb:
    def __init__(self, dbname):
        print u'初始化数据库操作'
        try:
            self.conn = MySQLdb.connect(host=db_host,user=db_name,passwd=db_passwd,port=db_port,use_unicode=True, charset='utf8')
            self.cur = self.conn.cursor()
            self.conn.select_db(db_dbname)

        except Exception, e:
            print u'数据库初始化失败:'+e.message
            logging.error(u'数据库初始化失败:'+e.message)
            exit(0)

    def get_url(self, web_name):
        try:
            self.cur.execute("SELECT id,link FROM links WHERE web_name = %s AND status<3 ORDER BY id ASC, status ASC", web_name)
            return self.cur.fetchone()
        except Exception, e:
            print (u'获取链接失败:'+web_name+':'+e.message)
            logging.error(u'获取链接失败:'+web_name+':'+e.message)
            exit(0)

    def check_url(self, url):
        try:
            md5 = hashlib.md5(url).hexdigest()
            return self.cur.execute("SELECT * FROM links WHERE `md5`=%s", md5)
        except Exception, e:
            print (u'链接验证失败'+url+' :'+e.message)
            logging.error(u'链接验证失败'+url+' :'+e.message)

    def add_url(self, url, web_name):
        try:
            md5 = hashlib.md5(url).hexdigest()
            self.cur.execute("INSERT INTO links(`link`, `web_name`, `md5`)VALUES(%s, %s, %s)", [url, web_name, md5])
            self.conn.commit()

        except Exception, e:
            print (u'链接添加失败'+url+', '+web_name+':'+e.message)
            logging.error(u'链接添加失败'+url+', '+web_name+':'+e.message)

    def update_url(self, id):
        try:
            self.cur.execute("UPDATE links SET status = status+1 WHERE id=%s", id);
            self.conn.commit()
            return True
        except Exception,e:
            print (u'链接更新失败'+id+':'+e.message)
            logging.error(u'链接更新失败'+id+':'+e.message)

    def close(self):
        try:
            self.cur.close()
            self.conn.close()
        except Exception, e:
            print (u'数据库关闭失败'+id+':'+e.message)
            logging.error(u'数据库关闭失败'+id+':'+e.message)