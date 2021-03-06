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
    Object = None

    def __init__(self, db='sg'):
        self.db = db
        self.connect()

    #self.conn = MySQLdb.connect(user='24a',db='test',passwd='24abcdef',host='localhost',unix_socket='/tmp/mysql.sock')#,unix_socket='/tmp/mysql.sock'
    def connect(self):
        # print '==================='
        print self.db
        if self.db == 'sg':
            self.conn = MySQLdb.connect(user='24a',db='ilovedeals',passwd='24abcdef',host='10.144.129.241',unix_socket='/tmp/mysql.sock')#,unix_socket='/tmp/mysql.sock'
        elif self.db == 'my':
            self.conn = MySQLdb.connect(user='root',db='myilovedeals',passwd='ntucdbs911',host='localhost',unix_socket='/tmp/mysql.sock')#,unix_socket='/tmp/mysql.sock'
        elif self.db == 'test':
            #self.conn = MySQLdb.connect(user = 'root',db='test',passwd = 'LEsc2008',host='localhost')
            self.conn = MySQLdb.connect(user='root',db='test',passwd='ntucdbs911',host='localhost',unix_socket='/tmp/mysql.sock')

    def execute(self, sql, args=None):
        """
        :rtype : object
        """
        try:
            self.cursor = self.conn.cursor(cursorclass = MySQLdb . cursors . DictCursor)
            self.cursor.execute('SET NAMES utf8')
        except Exception, e:
            print '---------------'+e.message
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


    def close(self):
        try:
            if self.cursor:
                self.cursor.close()
        except Exception, e:
            print e.message+'---cursor'
        try:
            if self.conn:
                self.conn.close()
        except Exception, e:
            print e.message+'===conn'

    def __del__(self):
        self.close()
