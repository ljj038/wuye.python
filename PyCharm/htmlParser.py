#!/usr/bin/python
# coding=utf-8
from bs4 import BeautifulSoup
import re
import urlparse
from spiderLogger import SpiderLogger


class HtmlParser:
    def getLinkList(self, newUrl, sContent):
        try:
            print newUrl
            lLink = []
            soup = BeautifulSoup(markup=sContent, features='html.parser', from_encoding='utf-8')
            lLinkTmp = soup.find_all(name='a', attrs={'target': '_blank'}, href=re.compile(r'show.php\?hash=\w+'))
            if (len(lLinkTmp) > 0):
                for i in lLinkTmp:
                    lLink.append(urlparse.urljoin(newUrl, i['href']))
            else:
                SpiderLogger.log('soup get perpage a link fail[%s]' % newUrl)

        finally:
            return lLink

    def getTotalPage(self, newUrl, sContent):
        try:
            iPage = 0
            soup = BeautifulSoup(markup=sContent, features='html.parser', from_encoding='utf-8')
            objA = soup.find('a', attrs={'class': 'pager-last'})
            if (objA is not None):
                iPage = objA.get_text()
            else:
                SpiderLogger.log('get total page fail[%s]' % newUrl)

        finally:
            return iPage

    def getDownUrl(self, newUrl, sContent):
        try:
            sUrl = None
            soup = BeautifulSoup(markup=sContent, features='html.parser', from_encoding='utf-8')
            # <a id = "download" href = "down.php?date=1471008730&amp;hash=a52535b56561172cbae4ccc48af075feadc49601" > 点击此处下载种子 < / a >
            objA = soup.find('a', attrs={'id': 'download'}, href=re.compile(r'down.php\w+'))
            if (objA is not None):
                sUrl = objA['href']
            else:
                SpiderLogger.log('get down url fail[%s]' % newUrl)
        finally:
            return sUrl
