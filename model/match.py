# -*- coding: utf-8 -*-
__author__ = 'ShengYue'
import lxml
import lxml.etree
from lxml.html.clean import Cleaner
import re
class match:
    '''
    修复HTML
    创建XPATH对象
    '''
    def __init__(self, html, url):
        cleaner = Cleaner(style=True, scripts=True,page_structure=False, safe_attrs_only=False)
        html = cleaner.clean_html(html)
        del cleaner

        self.etree = lxml.html.fromstring(html)
        self.etree.make_links_absolute( base_url=url, resolve_base_href=True)

    '''
    获取所有可以匹配链接
    '''
    def get_all_links(self, link_match, url):
        links = []
        all_links = self.etree.xpath('//a')

        for match in link_match:
            regLink = re.compile(url+match.get('value'))
            for a in all_links:
                try:
                    href = a.get('href')
                except:
                    continue;
                if regLink.match(href) != None:
                    links.append(href)
                #else:
                    #print '失败', a.get('href')
        del all_links
        return links

    '''
    获取所有需要查询的信息
    '''
    def get_match_info(self, match, url=None):

        try:
            data = {}
            for param in match:
                name = param.get('name')
                ntree =  lxml.html.fromstring(lxml.etree.tostring(param))
                #
                node = ntree.xpath('//parsers/parser')[0]
                xpath = node.get('xpath')

                infoxpath = self.etree.xpath(xpath)
                try:
                    nodetype = node.get('type')

                    if nodetype == 'text':
                        data[name] = infoxpath[0].strip()

                    elif nodetype == 'array':
                        arr = []
                        for item in infoxpath:
                            if item.strip() == '':
                                continue;
                            arr.append(item.strip())
                        data[name] = arr

                    elif nodetype == 'pageurl':
                        data[name] = url

                    elif nodetype == 'html':
                        infohtml = lxml.etree.tostring(infoxpath[0],encoding="utf-8",method="html")
                        infohtml = infohtml.strip()
                        reg = re.compile(r'<[!/]?\b(?!(\bpre\b|\bli\b|\bp\b|\bbr\b|\bspan\b|\bimg\b))+\b\s*[^>]*>|[\s\r\n\t]+')
                        infohtml = reg.sub(' ',infohtml).strip()
                        data[name] = infohtml

                except:
                    data[name] = ''
                    print name,u'读取不出来'
                    continue
        except:
            print xpath,u'读取不出来'

        return data

    def match_tiantang(self, match, url):
        try:
            data = {}
            for param in match:
                name = param.get('name')
                ntree =  lxml.html.fromstring(lxml.etree.tostring(param))
                #
                node = ntree.xpath('//parsers/parser')[0]
                xpath = node.get('xpath')

                infoxpath = self.etree.xpath(xpath)

                try:
                    nodetype = node.get('type')
                    if nodetype == 'text':
                        data[name] = infoxpath[0].strip()
                    elif nodetype == 'array':
                        arr = []
                        for item in infoxpath:
                            if item.strip() == '':
                                continue;
                            arr.append(item.strip())
                        data[name] = arr

                    elif nodetype == 'pageurl':
                        data[name] = url

                    elif nodetype == 'html':
                        infohtml = lxml.etree.tostring(infoxpath[0],encoding="utf-8",method="html")
                        infohtml = infohtml.strip()
                        reg = re.compile(r'<[!/]?\b(?!(\bpre\b|\bli\b|\bp\b|\bbr\b))+\b\s*[^>]*>|[\s\r\n\t]+')
                        infohtml = reg.sub(' ',infohtml).strip()
                        data[name] = infohtml
                except:
                    data[name] = ''
                    print name,u'读取不出来'
                    continue
        except:
            #log.write('system.log',xpath+u'读取不出来')
            print xpath,u'读取不出来'

    '''
   获取所有需要查询的信息
   '''
    def get_match_info_test(self, match, url=None):

        try:
            data = {}
            for param in match:
                name = param.get('name')
                ntree =  lxml.html.fromstring(lxml.etree.tostring(param))
                #
                node = ntree.xpath('//parsers/parser')[0]
                xpath = node.get('xpath')

                infoxpath = self.etree.xpath(xpath)
                try:
                    nodetype = node.get('type')
                    if nodetype == 'text':
                        data[name] = infoxpath[0].strip()
                    elif nodetype == 'array':
                        arr = []
                        for item in infoxpath:
                            if item.strip() == '':
                                continue;
                            arr.append(item.strip())
                        data[name] = arr

                    elif nodetype == 'pageurl':
                        data[name] = url

                    elif nodetype == 'html':
                        infohtml = lxml.etree.tostring(infoxpath[0],encoding="utf-8",method="html")
                        infohtml = infohtml.strip()
                        reg = re.compile(r'<[!/]?\b(?!(\bpre\b|\bli\b|\bp\b|\bbr\b))+\b\s*[^>]*>|[\s\r\n\t]+')
                        infohtml = reg.sub(' ',infohtml).strip()
                        data[name] = infohtml
                except:
                    data[name] = ''
                    print name,u'读取不出来'
                    continue
        except:
            #log.write('system.log',xpath+u'读取不出来')
            print xpath,u'读取不出来'

        return data

#        print self.etree.xpath('//h1/text()')[0]
#        print self.etree.xpath('//h1/em/text()')[0]
#        com = self.etree.xpath("//div[@class='filmcontents']/node()/text()|//div[@class='filmcontents']/text()")
#        s = ''
#        for c in com:
#            s = s+ c
#        print s
#        #规则学习
#        d = self.etree.xpath(u"//div[@class='detail_intro']/table/tr/td[text()='上映日期：']/../td[last()]/text()")
#        print d[0]
    def close(self):
        del self.etree


