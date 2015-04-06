__author__ = 'ShengYue'
import sys, os, bsddb, math
import re

def fil(word):
    return not word.lower() in ('is','a','and','or','not','if','while','at')

def wordseg(filename):

    return filter(fil, re.findall(r'(\w+)', open(filename).read()))

def trainCategory((num, wordseg)):
    db = {}
    for word in wordseg:
        print word
        db[word]  = db.get(word, 0) + 1
    len_w = len(wordseg)
    return db, len_w

def categorizeDoc((db, len_w), total_len_w, wordseg):
    a = math.log(float(len_w) / total_len_w)
    len_db = len(db)
    for word in wordseg:
        if word in db:
            pw = float(db[word])
            a += math.log(pw/len_db)
        else:
            a += math.log(0.01 / len_db)
    return a

def train(wordsegs):
    return map(trainCategory, enumerate(wordsegs))


def categorize(total_len_w, doc, trains):
    lresult = []
    i = 0
    for cat in trains:
        lresult.append((categorizeDoc(cat, total_len_w, doc), i))
        i += 1
    print lresult
    return max(lresult)

if __name__ == '__main__':
    #trains = train([wordseg(trainname) for trainname in sys.argv[1:-1]])
    #total_len_w = reduce(lambda x, y : x + y[1], trains, 0)
    #print categorize(total_len_w, wordseg(sys.argv[-1]), trains)

    print wordseg('food.txt')
    exit()
    trains = train([wordseg('food.txt'),wordseg('travel.txt'),wordseg('attraction.txt'),wordseg('beauty.txt'),wordseg('products.txt'),wordseg('learning.txt'),wordseg('services.txt'),wordseg('fun.txt'),wordseg('other.txt')])
    total_len_w = reduce(lambda x, y : x + y[1], trains, 0)
    print trains
    print categorize(total_len_w, '$9.90 for Box of 6 Classic Flavour Cupcakes at #1 Baker Street in Upper Thomson (Worth $18). Premium Flavours Available ', trains)
