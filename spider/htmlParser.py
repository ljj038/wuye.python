#!/usr/bin/python
# coding=utf-8
from bs4 import BeautifulSoup
import re
import urlparse


class htmlParser:
    def _getLinks(self):
        try:
            linkList = self.soup.find_all('a', href=re.compile(r'/view/\d+.htm'))
            if(linkList is None):
                raise Exception("htmlParser._getLinks BeautifulSoup find_all('a') is None")

            linkList = []
            for link in linkList:
                linkList.append(urlparse.urljoin(self.url, link['href']))

            return linkList
        finally:
            pass

    def _getData(self):
        try:
            dataDict = {}
            title_node = self.soup.find('dd', attrs={'class': 'lemmaWgt-lemmaTitle-title'})
            if(title_node is None):
                print("htmlParser._getData BeautifulSoup find('dd') is None")
                return None
            h1_node = title_node.find('h1')
            # print(title_node)
            if(h1_node is None):
                print("htmlParser._getData BeautifulSoup find('dd') is None")
                return None
            dataDict['title'] = title_node.get_text()
            summary_node = self.soup.find('div', attrs={'class': 'lemma-summary'})
            if(summary_node is None):
                print("htmlParser._getData BeautifulSoup find('div') is None")
                return None
            dataDict['summary'] = summary_node.get_text()
            return dataDict
        finally:
            pass

    def parse(self, url, content):
        try:
            self.content = content
            self.url = url
            self.soup = BeautifulSoup(self.content, 'html.parser', from_encoding='utf-8')
            linkList = self._getLinks()
            dataDict = self._getData()
            return linkList, dataDict
        finally:
            pass
