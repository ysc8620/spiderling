# -*- coding: utf-8 -*-
__author__ = 'ShengYue'
import MySQLdb
import hashlib

db_host = '127.0.0.1'
db_name = 'root'
db_passwd = 'LEsc2008'
db_dbname = 'python'
db_port = 3306

class db:
    #self.conn = None
    def __init__(self):
        try:
            self.conn = MySQLdb.connect(host=db_host,user=db_name,passwd=db_passwd,port=db_port)
            self.cur = self.conn.cursor()
            #print self.cur
            '''创建数据库 如果数据库不存在'''
            #count = self.cur.execute("create database if not exists %s", db_dbname)
            #print count
            self.conn.select_db(db_dbname)

        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    '''
    获取网站下连接
    '''
    def get_url(self, web_name):
        self.cur.execute("SELECT * FROM links WHERE web_name = %s", web_name)
        return self.cur.fetchone()

    '''
    持久化连接
    '''
    def add_url(self, link, web_name):
        md5 = mdb5 = hashlib.md5(link).hexdigest()
        self.cur.execute("INSERT INTO links(`link`, `web_name`, `md5`)VALUES(%s, %s, %s)", [link, web_name, md5])
        self.conn.commit()

    '''
    检测连接是否存在
    '''
    def check_url(self, link):
        md5 = mdb5 = hashlib.md5(link).hexdigest()
        return self.cur.execute("SELECT * FROM links WHERE `md5` = %s", md5)
        #return self.cur.fetchone()

    '''
    关闭数据库
    '''
    def close(self):
        try:
            self.cur.close()
            self.conn.close()
        except:
            pass
