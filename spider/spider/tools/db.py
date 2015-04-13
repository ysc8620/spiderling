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
    db = 'sg'

    def __init__(self, db='sg'):
        self.connect()
        self.db = db

    def connect(self):
        if self.db == 'sg':
            self.conn = MySQLdb.connect(user='24a',db='ilovedeals',passwd='24abcdef',host='10.144.129.241',unix_socket='/tmp/mysql.sock')#,unix_socket='/tmp/mysql.sock'
        elif self.db == 'my':
            self.conn = MySQLdb.connect(user='24a',db='myilovedeals',passwd='24abcdef',host='localhost',unix_socket='/tmp/mysql.sock')#,unix_socket='/tmp/mysql.sock'

        #self.conn = MySQLdb.connect(user='24a',db='test',passwd='24abcdef',host='localhost',unix_socket='/tmp/mysql.sock')#,unix_socket='/tmp/mysql.sock'
        # self.conn = MySQLdb.connect(user = 'root',db='test',passwd = 'LEsc2008',host='localhost')

    def execute(self, sql, args=None):
        try:
            self.cursor = self.conn.cursor(cursorclass = MySQLdb . cursors . DictCursor)
            self.cursor.execute('SET NAMES utf8')
        except:
            self.connect()
            self.cursor = self.conn.cursor(cursorclass = MySQLdb . cursors . DictCursor)
            self.cursor.execute('SET NAMES utf8')

        try:
            if args is not None:
                self.cursor.execute(sql,args)
            else:
                self.cursor.execute(sql)
            self.conn.commit()
        except (AttributeError, MySQLdb.OperationalError):
            print 'Mysql execute error'
            logs('------ '+ time.strftime("%Y-%m-%d %H-%M-%S")+' Mysql execute error: '+sql)
        return self.cursor

    def __del__(self):
        try:
            self.cursor.close()
        except:
            pass
        try:
            self.conn.close()
        except:
            pass

    def close(self):
        if(self.cursor):
            self.cursor.close()
        self.conn.close()
