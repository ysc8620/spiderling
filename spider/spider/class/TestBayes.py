#-*- coding:utf-8-*-

from NaiveBayes import BayesClassifier
#from numpy import *
import MySQLdb

def create():
    conn = MySQLdb.connect(user = 'root',db='test',passwd = 'LEsc2008',host='localhost')
    cursor = conn.cursor(cursorclass = MySQLdb . cursors . DictCursor)
    cursor.execute('SET NAMES utf8')
    res = cursor.execute('SELECT * FROM le_goods_cate_keywords')
    e = cursor.fetchall()
    i1 = []
    i2 = []
    i3 = []
    i4 = []
    i5 = []
    i6 = []
    i7 = []
    i8 = []
    i9 = []


    features=[]            #数据集特征集
    labels=[]                #数据集类标集
    for i in e:
        #print i

        #print i['cate_id'], i['keyword']
        if i['cate_id'] == 1:
            i1.append(i['keyword'])
        if i['cate_id'] == 2:
            i2.append(i['keyword'])
        if i['cate_id'] == 3:
            i3.append(i['keyword'])
        if i['cate_id'] == 4:
            i4.append(i['keyword'])
        if i['cate_id'] == 5:
            i5.append(i['keyword'])
        if i['cate_id'] == 6:
            i6.append(i['keyword'])
        if i['cate_id'] == 7:
            i7.append(i['keyword'])
        if i['cate_id'] == 8:
            i8.append(i['keyword'])
        if i['cate_id'] == 9:
            i9.append(i['keyword'])
    labels.append('1')
    features.append(i1)

    labels.append('2')
    features.append(i2)

    labels.append('3')
    features.append(i3)

    labels.append('4')
    features.append(i4)

    labels.append('5')
    features.append(i5)

    labels.append('6')
    features.append(i6)

    labels.append('7')
    features.append(i7)

    labels.append('8')
    features.append(i8)

    labels.append('9')
    features.append(i9)

    Bay=BayesClassifier()
    Bay.train(features,labels)

    # print features
    # print labels
    print Bay.classify("JUMBO Seafood NSRCC: $65 for $100 Cash Voucher at Changi Coast Walk. More Options Available ")

def main():
    file=open("./Weather.txt",'r')
    features=[]            #数据集特征集
    labels=[]                #数据集类标集
    for line in file:         #一行行读数据文件
        line=line.strip()
        tempVec=line.split(',')
        labels.append(tempVec[len(tempVec)-1])
        tempVec2=[tempVec[i] for i in range(0,len(tempVec)-1)]
        features.append(tempVec2)
    Bay=BayesClassifier()
    Bay.train(features,labels)
    correct=0
    for i in range(0,len(features)):
        #print features[i]
        label=Bay.classify(features[i])
        #print("Original:"+str(labels[i])+"==>"+"Classified:"+label)
        if str(label)==str(labels[i]):
            correct+=1
    #print Bay.classify('mild')
    #print("Accuracy:",correct/len(features))    #正确率
    print features
    print labels
if __name__=='__main__':
    create()