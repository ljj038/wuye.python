#!/usr/bin/python
# -*- coding: utf-8 -*-
from loggerSpider import loggerSpider
import re
from bs4 import BeautifulSoup


class htmlParser:
    def __init__(self):
        pass

    def urlParse(self, content, newUrl):
        hrefList = []
        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        aList = soup.find_all('a', href=re.compile(r'http://[a-z-./]+/\d+/$', re.I))
        if(len(aList) == 0):
            loggerSpider.log('find_all is empty [%s]' % (newUrl))
        else:
            for a in aList:
                if((a.get('href', None) is not None) and (a.get('title', None) is not None)):
                    hrefList.append(a['href'])

        return hrefList

    def perPageParse(self, content, newUrl):
        newDataDict = {}
        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        div_node = soup.find('div', attrs={'class': 'entry-header'})
        if(div_node is None):
            loggerSpider.log('div_node is None [%s]' % (newUrl))

        h1_node = div_node.find('h1')
        if(h1_node is None):
            loggerSpider('h1_node is None [%s]' % (newUrl))
        else:
            newDataDict['title'] = h1_node.get_text()
            newDataDict['href'] = newUrl

        entry_node = soup.find('div', attrs={'class': 'entry'})
        if(entry_node is None):
            loggerSpider.log('entry_node is None [%s]' % (newUrl))
        else:
            newDataDict['content'] = entry_node.get_text()

        newUrlList = self.urlParse(content, newUrl)
        return newUrlList, newDataDict
