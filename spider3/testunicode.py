#!/usr/bin/env python
# coding=utf-8
__author__ = 'zhaoyingnan'
import htmlLoader
from bs4 import BeautifulSoup


class Test:
    def __init__(self):
        self.htmlLoader = htmlLoader.htmlLoader()

    def excute(self):
        listAContent = []
        sContent = self.htmlLoader.htmlDown('http://www.kuqin.com/shuoit/20160830/352805.html')
        sContent = sContent.decode('GBK').encode('UTF-8')  # 必须在这里先将编码转换为utf8
        # print sContent
        # print type(sContent)
        # exit()
        soup = BeautifulSoup(sContent, 'html.parser', from_encoding='utf-8')
        aNode = soup.find_all('a')
        if (aNode is not None):
            for node in aNode:
                # listAContent.append(node.get_text().decode('GBK').encode('UTF-8'))  # 在这里不行
                listAContent.append(node.get_text())

        print listAContent
        # exit()
        s = ','.join(listAContent)

        print s


if (__name__ == '__main__'):
    demo = Test()
    demo.excute()
