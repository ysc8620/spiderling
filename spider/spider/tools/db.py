#!/usr/bin/python
#coding=utf-8
from common import *
import sys,os
import time
reload(sys)
sys.setdefaultencoding('utf8')
import MySQLdb

class DB:
    conn = None
    cursor = None
    def connect(self):
        #self.conn = MySQLdb.connect (host = DB_Host,   user = DB_User,  passwd = DB_PWD,  db = DB_DB)
        #self.conn = MySQLdb.connect(user = '24a',db='ilovedeals',passwd = '24abcdef',host='10.144.129.241',unix_socket='/tmp/mysql.sock')#,unix_socket='/tmp/mysql.sock'
        if self.conn:
            pass
        else:
            #self.conn = MySQLdb.connect(user='24a',db='ilovedeals',passwd='24abcdef',host='10.144.129.241',unix_socket='/tmp/mysql.sock')#,unix_socket='/tmp/mysql.sock'
            self.conn = MySQLdb.connect(user='24a',db='test',passwd='24abcdef',host='localhost',unix_socket='/tmp/mysql.sock')#,unix_socket='/tmp/mysql.sock'
            #self.conn = MySQLdb.connect(user = 'root',db='test',passwd = 'LEsc2008',host='localhost')

    def execute(self, sql, args=None):
        self.connect()
        try:
            cursor = self.conn.cursor(cursorclass = MySQLdb . cursors . DictCursor)
            cursor.execute('SET NAMES utf8')
            if args is not None:
                cursor.execute(sql,args)
            else:
                cursor.execute(sql)
            self.conn.commit()
        except (AttributeError, MySQLdb.OperationalError):
            print 'Mysql execute error'
            logs('------ '+ time.strftime("%Y-%m-%d %H-%M-%S")+' Mysql execute error: '+sql)
        return cursor

    def close(self):
        if(self.cursor):
            self.cursor.close()
        self.conn.close()