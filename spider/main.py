from Classy import *
import MySQLdb
from collections import Counter

conn = MySQLdb.connect(user = 'root',db='test',passwd = 'LEsc2008',host='localhost')

cursor = conn.cursor(cursorclass = MySQLdb . cursors . DictCursor)
cursor.execute('SET NAMES utf8')

rs = cursor.execute('SELECT * FROM t_tag_cate_keyword')
data = cursor.fetchall()
classData = {}


for i in data:
    if not classData.has_key('c'+str(i['cate_id'])):
        classData['c'+str(i['cate_id'])] = []
    classData['c'+str(i['cate_id'])].append(i['keyword'].strip())

for i in classData:
    print i, classData[i]

c = Classy()
for i in classData:
    print c.train(classData[i],i)

data = 'jewellery'
d =  data.split()
my_office = ['Cash', 'Voucher','Food', 'Drinks','Bakerzin','Multiple','Outlets']
print c.classify(my_office)