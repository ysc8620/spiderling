#-*-coding:utf-8-*-
__author__ = 'ShengYue'
import re
from pymongo import Connection


#rer = re.compile(r"(new-products|top-sellers|special-price).*?")
res = re.match(r".*?/(new-products|top-sellers|special-price|faq|brands|payment-methods|howtoshop|about|affiliate)/", 'http://www.lazada.sg/special-price/?page=2')
print res.group(1)
exit()
con = Connection('localhost', 27017)
db = con.test
posts = db.tname

#posts.insert({'_id':'111', 'name':'xxx'})
res =  posts.find({'name':'---'})

print res.count()
for s in res:
    print s
if res:
    print '111'
else:
    print '222'

#open('lazada.log','a+').write('aaaaaaaaaaaaa'+"\r")

res = re.match(r'http://www.lazada.sg/.+','http://www.lazada.sg/zwilling-ja-/henckels-twin-pollux-6pc-knife-block-set-43836.html?sdds' )
if res:
    print 2
    #print res.group(0)
else:
    print 1