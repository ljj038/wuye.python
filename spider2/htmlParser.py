#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import urlparse


class htmlParser:

    # 获取每个页面的所有的<a></a>标签的地址
    def __parseNewLink(self, soup, newUrl):
        # 获取所有的<a></a>标签的href地址
        newLinkList = []
        linkList = soup.find_all('a', href=re.compile(r'/view/\d+.htm'))
        # print(linkList)
        if(linkList is not None):
            for link in linkList:
                newLinkList.append(urlparse.urljoin(newUrl, link['href']))
        return newLinkList

    # 获取每个页面的信息
    def __parseNewData(self, soup, newUrl):
        newDataDict = {}

        # 获取title
        title_node = soup.find('dd', attrs={'class': 'lemmaWgt-lemmaTitle-title'})
        if(title_node is None):
            print("[%s] title_node is None" % (newUrl))
        else:
            h1_node = title_node.find('h1')
            if(h1_node is None):
                print("[%s] h1_node is None" % (newUrl))
            else:
                newDataDict['title'] = h1_node.get_text()

        # 获取总结
        summary_node = soup.find('div', attrs={'class': 'lemma-summary'})
        if(summary_node is None):
            print("[%s] summary_node is None" % (newUrl))
        else:
            newDataDict['summary'] = summary_node.get_text()

        return newDataDict

    def parse(self, content, newUrl):
        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        newLinkList = self.__parseNewLink(soup, newUrl)
        newDataDict = self.__parseNewData(soup, newUrl)
        return newLinkList, newDataDict
