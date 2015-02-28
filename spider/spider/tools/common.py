#-*-coding:utf-8-*-

__author__ = 'ShengYue'
import hashlib

def get_seo_title(str):
    try:
        import re
        vocalMap = { 'a' : ['&agrave;','&aacute;','&acirc;','&atilde;','&auml;','&aring;','&aelig;','&#224;','&#225;','&#226;','&#227;','&#228;','&#229;','&#257;','&#230;'],
                     'e' : ['&egrave;','&eacute;','&ecirc;','&euml;','&#232;','&#233;','&#234;','&#235;','&#275;'],
                     'i' : ['&igrave;','&iacute;','&icirc;','&iuml;','&#236;','&#237;','&#238;','&#239;','&#299;'],
                     'o' : ['&ograve;','&oacute;','&ocirc;','&oelig;','&otilde;','&ouml;','&#242;','&#243;','&#244;','&#339;','&#245;','&#246;','&#333;'],
                     'u' : ['&ugrave;','&uacute;','&ucirc;','&uuml;','&#249;','&#250;','&#251;','&#252;','&#363;']
                    }

        str = str.strip().lower()

        for vocale, lista in vocalMap.iteritems(): #per ogni elemento della mappa avrà una chiave ed una lista
            for elemento in lista: #itero su tutti gli elementi della lista
                str = str.replace(elemento,vocale) #sostituisco nel nome dell'offerta, la vocale all' HTML-entity
                
        str = str.replace("/","-")
        str = re.sub("[^a-z0-9_\s-]","",str)     #######################################
        str = re.sub("[\s-]+"," ",str)           #strippo tutti i caratteri non voluti:#
        str = re.sub("[\s_]","-",str)            #######################################
    except:
        pass

    str = (str if len(str)  > 2 else 'details') # len(str) < 2 ? str : 'details'
    return str.strip('-')

def get_img_path(url, type='original'):
    image_guid = hashlib.sha1(url).hexdigest()
    path = image_guid[0:2]
    return '/uploaded/'+type+'/%s/%s.jpg' % (path, image_guid)

def logs(str):
    file("./error.log","a+").write(str+"\r")

