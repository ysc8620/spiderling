#-*-coding:utf-8-*-
from goose import Goose
from goose.text import StopWordsChinese
url  = 'http://news.cnblogs.com/n/504072/'
g = Goose({'stopwords_class': StopWordsChinese})
article = g.extract(url=url)
print article.canonical_link

