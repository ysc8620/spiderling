# -*- coding: utf-8 -*-
__author__ = 'ShengYue'
import lxml
import lxml.etree
from lxml.html.clean import Cleaner
import re
from log import *

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
            regLink = re.compile(url + match.get('value'))
            for a in all_links:
                href = a.get('href')
                if href == None:
                    continue

                if regLink.match(href) != None:
                    links.append(href)

        del all_links
        return links

    '''
    验证是否是详细页链接
    '''
    def check_info_link(self, link_match, url):
        for match in link_match:
            regLink = re.compile(match.get('value'))

            if regLink.match(url) != None:
                return True
            else:
                return False

    def match_info(self, match):
        try:
            retrun_data = {}
            for param in match:
                # 匹配当前配置项
                name = param.get('name')
                if name == None:
                    logging.error(u'无法获取字段名')
                    return
                param_tree = lxml.html.fromstring(lxml.etree.tostring(param))

                # 匹配单独项所有规则
                for node in param_tree.xpath('//parsers/parser'):
                    xpath = node.get('xpath')
                    type = node.get('type')
                    info_tree = self.etree.xpath(xpath)

                    try:
                        if type == None:
                            logging.error('字段数据类型获取不到'+name)

                        # 纯文本字段
                        elif type == 'text':
                            retrun_data[name] = ''
                            for val in info_tree:
                                retrun_data[name] = val.strip()

                        elif type == 'text_array':
                            arr = []
                            retrun_data[name] = arr
                            for val in info_tree:
                                if val.strip() == '':
                                    continue
                                arr.append(val.strip())
                            retrun_data[name] = arr

                        elif type == 'html':
                            retrun_data[name] = ''
                            for val in info_tree:
                                infohtml = lxml.etree.tostring(val,encoding="utf-8",method="html")
                                infohtml = infohtml.strip()
                                reg = re.compile(r'<[!/]?\b(?!(\bpre\b|\bli\b|\bp\b|\bbr\b|\bspan\b|\bimg\b))+\b\s*[^>]*>|[\s\r\n\t]+')
                                infohtml = reg.sub(' ',infohtml).strip()
                                retrun_data[name] = infohtml

                    except Exception, e:
                        print e.message;
        except Exception, e:
            logging.error(u'获取详细信息失败: '+e.message())


    def close(self):
        del self.etree



