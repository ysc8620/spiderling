# -*- coding: utf-8 -*-
__author__ = 'ShengYue'
from lxml import etree
from model.curl import curl
from lxml.html.clean import Cleaner
import lxml
import re
import MySQLdb
#from lxml.html import html
url = u'http://www.ffdy.cc/type/movie/'
data = {}
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='LEsc2008',port=3306)
    cur=conn.cursor()

    #cur.execute('create database if not exists python')
    conn.select_db('python')
    #cur.execute('create table test(id int,info varchar(20))')

    #value=[1,'hi rollen']
    #cur.execute('insert into test values(%s,%s)',value)

    #values=[]
    #for i in range(20):
     #   values.append((i,'hi rollen'+str(i)))

    #cur.executemany('insert into test values(%s,%s)',values)

    #cur.execute('update test set info="I am rollen" where id=3')



except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def getUrl(url=None):

    if url == None:
        count=cur.execute("select id,url,status from urllist where status = 0 limit 1")
        if count == 0:
            print u'遍历完成'
            print count
            return 0
        res = cur.fetchone()
        #print res
        url = res[1]
        cur.execute ("UPDATE urllist SET status=1 WHERE id="+str(res[0]))
        conn.commit()
    else:
        count = 1
    print u'读取链接:'+url
    #url = urllib2.
    curls = curl()
    html = curls.read(url)
    if html == '':
        getUrl()
        return 0

    cleaner = Cleaner(style=True, scripts=True,page_structure=False, safe_attrs_only=False)
    htmml = cleaner.clean_html(html)

    #xtree = etree.HTML(htmml)
    #links = xtree.xpath('//a')
    XHTML = lxml.html.fromstring(htmml)
    XHTML.make_links_absolute( base_url=url, resolve_base_href=True)

    links = XHTML.xpath('//a')
    regLink = re.compile(r'http://www.ffdy.cc/(type/movie|movie)')
    #print '----'
    #print links
    for a in links:
        #print a.get('href')
        if regLink.match(a.get('href')) != None:
            print '====',a.get('href')
            counts=cur.execute("select id from urllist where url=%s", a.get('href'))
            #print a.get('href')
            #print '---111'
            #print count
            if counts == 0:
                cur.execute("insert into urllist(url)values(%s)",a.get('href'))
                conn.commit()
                #print
                #getUrl(a.get('href'))
    if count >0:
        print u'重复'
        getUrl()
            #getUrl(a.get('href'))
    #print a.get('href')


try:
    getUrl(url)

    cur.close()
    conn.close()
except:
    print "Mysql Error "

#import urllib

#print 'http://www.ffdy.cc/type,area/movie,czech%20republic'
#print urllib.unquote( 'http://www.ffdy.cc/type,area/movie,czech%20republic')