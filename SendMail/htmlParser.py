#!/usr/bin/env python
# coding=utf-8
__author__ = 'zhaoyingnan'
from bs4 import BeautifulSoup


class HtmlParser:
    def parse(self, sContent):
        sTitle = None
        soup = BeautifulSoup(sContent, 'html.parser', from_encoding='utf-8')
        titleNode = soup.find('title')
        if (titleNode is not None):
            sTitle = titleNode.get_text()

        return sTitle
