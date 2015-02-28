#!/usr/bin/python
#coding=utf-8

import sys,os
reload(sys)
sys.setdefaultencoding('utf8')
import MySQLdb
DB_Host = ''
DB_User = 'root'
DB_PWD = ''
DB_DB = ''

class DB:
  conn = None
  cursor = None
  def connect(self):
    #self.conn = MySQLdb.connect (host = DB_Host,   user = DB_User,  passwd = DB_PWD,  db = DB_DB)
    #self.conn = MySQLdb.connect(user = '24a',db='ilovedeals',passwd = '24abcdef',host='10.144.129.241',unix_socket='/tmp/mysql.sock')#,unix_socket='/tmp/mysql.sock'
    self.conn = MySQLdb.connect(user = 'root',db='test',passwd = 'LEsc2008',host='localhost')


  def execute(self, sql, args=None):
    try:
      cursor = self.conn.cursor(cursorclass = MySQLdb . cursors . DictCursor)
      cursor.execute('SET NAMES utf8')
      if args is not None:
        cursor.execute(sql,args)
      else:
        cursor.execute(sql)
      self.conn.commit()
    except (AttributeError, MySQLdb.OperationalError):
      self.connect()
      cursor = self.conn.cursor(cursorclass = MySQLdb . cursors . DictCursor)
      cursor.execute('SET NAMES utf8')
      if args is not None:
        cursor.execute(sql,args)
      else:
        cursor.execute(sql)
      self.conn.commit()
    return cursor

  def close(self):
    if(self.cursor):
      self.cursor.close()
    self.conn.close()