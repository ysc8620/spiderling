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
            self.conn = MySQLdb.connect(host=db_host,user=db_name,passwd=db_passwd,port=db_port,use_unicode=True, charset='utf8')
            self.cur = self.conn.cursor()

            #print self.cur
            '''创建数据库 如果数据库不存在'''
            #count = self.cur.execute("create database if not exists %s", db_dbname)
            #print count
            self.conn.select_db(db_dbname)
            #self.cur.execute("SET NAMES utf8")

        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    '''
    获取网站下连接
    '''
    def get_url(self, web_name):
        self.cur.execute("SELECT * FROM links WHERE web_name = %s AND status=0", web_name)
        return self.cur.fetchone()

    '''
    持久化连接
    '''
    def add_url(self, link, web_name):
        md5 = hashlib.md5(link).hexdigest()
        print link
        self.cur.execute("INSERT INTO links(`link`, `web_name`, `md5`)VALUES(%s, %s, %s)", [link, web_name, md5])
        self.conn.commit()

    '''
    检测连接是否存在
    '''
    def check_url(self, link):
        md5 = mdb5 = hashlib.md5(link).hexdigest()
        return self.cur.execute("SELECT * FROM links WHERE `md5`=%s", md5)
        #return self.cur.fetchone()

    def update_url(self, id):
        self.cur.execute("UPDATE links SET status = 1 WHERE id=%s", id);
        self.conn.commit()
        return True

    def add_star(self, director):
        #print director
        count = self.cur.execute("SELECT id FROM star WHERE name=%s", director)
        if count == 0:
            self.cur.execute("INSERT INTO star(name)VALUES(%s)",director)

            id = self.conn.insert_id()
            self.conn.commit()
            return str(id)
        else:
            star = self.cur.fetchone()
            return str(star[0])

    def addData(self,data):
        #print data
        ### 增加导演
        director = ''
        try:
            for daoyan in data['director']:
                director += ','+self.add_star(daoyan)
            director = director.strip(',')
        except:
            director = ''

        ### 增加主演
        leading = ''
        try:
            for lead in data['leading']:
                leading += ','+self.add_star(lead)
            leading = leading.strip(',')
        except:
            leading = ''

        ### 简介
        comment = ''
        try:
            for comm in data['comment']:
                comment += comm
        except:
            comment = '';
        #标题， 图片, 链接
        inserData = [data['title'], data['detail_pic'],data['url'],director,leading,data['area'],data['show_day'],comment]
        self.add_movie(inserData)

    def add_movie(self,insertData):
        self.cur.execute("INSERT INTO movie(`title`,`img`,`url`,`director`,`leading`,`area`,`show_day`,`comment`)VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", insertData)
        self.conn.commit()

    '''
    关闭数据库
    '''
    def close(self):
        try:
            self.cur.close()
            self.conn.close()
        except:
            pass
