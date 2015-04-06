__author__ = 'ShengYue'
#!/usr/bin/python
#coding=utf-8
import re
import sys

reload(sys)

sys.setdefaultencoding('utf8')

url = 'http://www.courts.com.sg/Products/PID-IP093630EXDP(Courts)/Home-Entertainment/TV/LEDs/40-to-44/PHILIPS-40-IN-FULL-HD-LED-LCD-TV-WITH2-SIDED-AMBILIGHT-40PFT5509-98'
res = re.match(re.compile('http://www.courts.com.sg/Products/PID-.+$'), url)
print res.group()