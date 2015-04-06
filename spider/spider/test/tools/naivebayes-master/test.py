from naivebayes import NaiveBayes
import MySQLdb
classes = {'chinese': [['chinese', 'beijing', 'chinese'],
                       ['chinese', 'chinese', 'shanghai'],
                       ['chinese', 'macao']],
           'japanese': [['tokyo', 'japan', 'chinese']]}

test_document = ['chinese', 'chinese', 'chinese', 'tokyo', 'japan']

# for klass in classes:
#     print("Documents for class '%s'" % klass)
#     for document in classes[klass]:
#         print(', '.join(document))
#     print('')


conn = MySQLdb.connect(user = 'root',db='test',passwd = 'LEsc2008',host='localhost')
cursor = conn.cursor(cursorclass = MySQLdb . cursors . DictCursor)
cursor.execute('SET NAMES utf8')
res = cursor.execute('SELECT * FROM t_tag_cate_keyword')
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
features=[]
labels=[]
for i in e:

    #print i['cate_id'], i['keyword']  travel
    #print i
    if i['cate_id'] == 1:
        i1.append(i['keyword'])
        open('travel.txt','a+').write(i['keyword']+"\n")
    if i['cate_id'] == 2:
        i2.append(i['keyword'])
        open('food.txt','a+').write(i['keyword']+"\n")
    if i['cate_id'] == 3:
        i3.append(i['keyword'])
        open('beauty.txt','a+').write(i['keyword']+"\n")
    if i['cate_id'] == 4:
        i4.append(i['keyword'])
        open('attraction.txt','a+').write(i['keyword']+"\n")
    if i['cate_id'] == 5:
        i5.append(i['keyword'])
        open('fun.txt','a+').write(i['keyword']+"\n")
    if i['cate_id'] == 6:
        i6.append(i['keyword'])
        open('learning.txt','a+').write(i['keyword']+"\n")
    if i['cate_id'] == 7:
        i7.append(i['keyword'])
        open('services.txt','a+').write(i['keyword']+"\n")
    if i['cate_id'] == 8:
        i8.append(i['keyword'])
        open('products.txt','a+').write(i['keyword']+"\n")
    if i['cate_id'] == 9:
        i9.append(i['keyword'])
        open('other.txt','a+').write(i['keyword']+"\n")

classes = {'c1':[i1], 'c2':[i2], 'c3':[i3],'c4':[i4],'c5':[i5],'c6':[i6],'c7':[i7],'c8':[i8],'c9':[i9]}

classifier = NaiveBayes()

classifier.train(classes)
#
# scores = classifier.scores(test_document)
#
# print("Class scores")
# for klass in scores:
#     print("%s: %f" % (klass, scores[klass]))
# print('')

def getss(str):
    return str.strip().split(" ")

test_document = getss('Insulated Lunch Box')
print test_document
classification = classifier.classify(test_document)

print("Classified as '%s'" % classification)
