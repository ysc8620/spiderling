#!/usr/bin/python
#coding=utf-8
import sys,os
import time, datetime, math
reload(sys)
sys.setdefaultencoding('utf8')

'''
/**
 * 商品排序定时执行程序。
 * <li>公式1:
 * <p>score = p-1/(t+1)^1.8</p>
 * <p>score = countView/(addTime+1)^1.8</p>
 * </li>
 * <li>公式2:
 * <p>score = log10(Z) + yt/45000</p>
 * <p>x = 赞成票 - 反对票</p>
 * <p>if (x != 0) { Z = |x| }</p>
 * <p>if (x == 0) { Z = 1 }</p>
 * <p>if (x > 0) y = 1</p>
 * <p>if (x == 0) y = 0</p>
 * <p>if (x < 0) y = -1</p>
 * <p>t = 创建时间 - 网站成立时间</p>
 *
 * </li>
 */
# '''
# a = "24"
# now_time = datetime.datetime.now()
#
# b = now_time + datetime.timedelta(hours=24)
# print time.mktime (time.strptime(str(b)[:19],'%Y-%m-%d %H:%M:%S'))

class GoodsOrder:
    def __init__(self):
        pass

    def execute(self):
        #公式2
        #如果24小时内的都取当前时间作为商品的创建时间
        addtime = time.time() - 1000
        countView =12
        if (time.time() - addtime < 86400):
            addtime = int(time.time())

        t = addtime - time.mktime (time.strptime('2012-04-25 19:30','%Y-%m-%d %H:%M'))

        x = countView

        z = 1;
        if (x != 0):
            z = math.fabs(x)

        y = 0
        if (x >= 0):
            y = 1
        elif (x < 0):
            y = -1

        score = math.log(z)/math.log(3) + float(y*t)/(24*3600)#12小时
        return score

g = GoodsOrder()
g.execute()