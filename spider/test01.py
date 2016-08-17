#!/usr/bin/python
# coding=utf-8
import re
import urllib2
import urlparse
from bs4 import BeautifulSoup

rootUrl = 'http://baike.baidu.com/view/48530.htm'
response = urllib2.urlopen(rootUrl)
code = response.getcode()
if(code != 200):
    print("urlopen fail")
    exit()

soup = BeautifulSoup(response.read(), 'html.parser', from_encoding='utf-8')
title_node = soup.find('dd', attrs={'class': 'lemmaWgt-lemmaTitle-title'})
if(title_node is None):
    print('title_node is None')
    exit()

h1_node = title_node.find('h1')
if(h1_node is None):
    print('h1_node is None')
    exit()

title = h1_node.get_text()
print(title)


linkList = soup.find_all('a', href=re.compile(r'/view/\d+.htm'))
if(linkList is not None):
    for link in linkList:
        print(urlparse.urljoin(rootUrl, link['href']))
