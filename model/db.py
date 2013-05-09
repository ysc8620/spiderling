# -*- coding: utf-8 -*-
__author__ = 'ShengYue'
import hashlib
import sqlite3
from log import *

'''
链接管理
'''
class linkdb:
    def __init__(self, dbname):
        try:
            self.conn = sqlite3.connect(':memory:')
            # 创建临时表
            self.cur = self.conn.cursor()

            # 创建内存表
            self.cur.execute('''CREATE TABLE IF NOT EXISTS `links` (
              `id` INTEGER  PRIMARY KEY AUTOINCREMENT,
              `link` varchar(300) NOT NULL,
              `web_name` varchar(16) NOT NULL,
              `md5` varchar(32) NOT NULL,
              `status` tinyint(1) NOT NULL DEFAULT '0'
            );''')

            self.cur.execute('''CREATE INDEX IF NOT EXISTS status on links (status);''')
            self.cur.execute('''CREATE INDEX IF NOT EXISTS md5 on links (md5);''')
            self.cur.execute('''CREATE INDEX IF NOT EXISTS web_name on links (web_name);''')
            #self.conn.commit()

        except Exception, e:
            logging.error(u'数据库初始化失败:'+e.message)
            exit(0)

    def get_url(self, web_name):
        try:
            self.cur.execute("SELECT * FROM links WHERE web_name = %s AND status=0", web_name)
            return self.cur.fetchone()
        except Exception, e:
            logging.error(u'获取链接失败:'+web_name+':'+e.message)
            exit(0)

    def check_url(self, url):
        try:
            md5 = hashlib.md5(url).hexdigest()
            return self.cur.execute("SELECT * FROM links WHERE `md5`=%s", md5)
        except Exception, e:
            logging.error(u'链接验证失败'+url+':'+e.message)

    def add_url(self, url, web_name):
        try:
            md5 = hashlib.md5(url).hexdigest()
            self.cur.execute("INSERT INTO links(`link`, `web_name`, `md5`)VALUES(%s, %s, %s)", [url, web_name, md5])
            #self.conn.commit()

        except Exception, e:
            logging.error(u'链接添加失败'+url+', '+web_name+':'+e.message)

    def update_url(self, id):
        try:
            self.cur.execute("UPDATE links SET status = 1 WHERE id=%s", id);
            #self.conn.commit()
            return True
        except Exception,e:
            logging.error(u'链接更新失败'+id+':'+e.message)

    def close(self):
        try:
            self.cur.close()
            self.conn.close()
        except Exception, e:
            logging.error(u'数据库关闭失败'+id+':'+e.message)