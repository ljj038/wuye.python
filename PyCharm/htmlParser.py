#!/usr/bin/python
# coding=utf-8
from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser:
    def getLinkList(self, newUrl, sContent):
        try:
            lLink = []
            print(newUrl)
            soup = BeautifulSoup(markup=sContent, features='html.parser', from_encoding='utf-8')
            lLinkTmp = soup.find_all(name='a', attrs={'target': '_blank'}, href=re.compile(r'show.php\?hash=\w+'))
            if (len(lLinkTmp) > 0):
                for i in lLinkTmp:
                    lLink.append(urlparse.urljoin(newUrl, i['href']))

        finally:
            return lLink