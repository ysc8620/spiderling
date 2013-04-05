# -*- coding: utf-8 -*-
__author__ = 'ShengYue'
import lxml
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
                if regLink.match(a.get('href')) != None:
                    links.append(a.get('href'))
                #else:
                    #print '失败', a.get('href')
        del all_links
        return links

    def close(self):
        del self.etree


