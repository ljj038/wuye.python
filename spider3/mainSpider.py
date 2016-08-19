#!/usr/bin/python
# -*- coding: utf-8 -*-
import htmlLoader
from loggerSpider import loggerSpider
import urlManager
import htmlParser
import dataHandler


class Spider:
    def __init__(self):
        self.htmlLoader = htmlLoader.htmlLoader()
        self.urlManager = urlManager.urlManager()
        self.htmlParser = htmlParser.htmlParser()
        self.dataHandler = dataHandler.dataHandler()

    def execute(self, newUrl, isFirst=False):
        i = 1
        self.urlManager.addOneUrl(newUrl)
        while(True):
            newUrlList = []
            newDataDict = {}
            try:
                if(self.urlManager.hasMoreUrls() > 0):
                    getOneUrl = self.urlManager.getOneUrl()
                    content = self.htmlLoader.htmlDown(getOneUrl)
                    if(content is None):
                        continue

                    if(i == 1):
                        # 解析首页
                        newUrlList = self.htmlParser.urlParse(content, getOneUrl)
                    else:
                        # 解析每个页面
                        newUrlList, newDataDict = self.htmlParser.perPageParse(content, getOneUrl)

                    # print(newUrlList)
                    if(len(newUrlList) > 0):
                        self.urlManager.addUrls(newUrlList)

                    if(len(newDataDict) > 0):
                        self.dataHandler.insert(newDataDict)
                else:
                    loggerSpider.log('has no more url')
                    break
            except Exception as e:
                loggerSpider.log(e)

            i += 1

if(__name__ == '__main__'):
    urlList = ['http://www.jobbole.com/', 'http://python.jobbole.com/', 'http://blog.jobbole.com/category/php-programmer/']
    spider = Spider()
    for url in urlList:
        spider.execute(url)
