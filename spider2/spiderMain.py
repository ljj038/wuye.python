#!/usr/bin/python
# -*- coding: utf-8 -*-
import urlManager
import htmlParser
import htmlLoader
import htmlDrawer
import traceback


class Spider:
    """a spider test"""
    def __init__(self):
        self.newDataList = []
        self.urlManager = urlManager.urlManager()
        self.htmlParser = htmlParser.htmlParser()
        self.htmlLoader = htmlLoader.htmlLoader()
        self.htmlDrawer = htmlDrawer.htmlDrawer()

    def execute(self, rootUrl):
        try:
            i = 1
            while(True):
                if(i == 100):
                    break
                # 添加开始的url
                self.urlManager.addNewUrl(rootUrl)
                # 判断是否有更多的url
                if(self.urlManager.hasMoreUrl() > 0):
                    # 获取一个新的url
                    newUrl = self.urlManager.getOneUrl()
                    # print(newUrl)
                    # 抓取url的内容
                    content = self.htmlLoader.urlLoad(newUrl)
                    # print(content)
                    if(content is None):
                        print("%s 内容获取失败" % (newUrl))
                    else:
                        # 解析url
                        newLinkList, newDataDict = self.htmlParser.parse(content, newUrl)
                        # print(newLinkList)
                        # print(newDataDict)

                        # 将新的url添加到url管理器中
                        if(len(newLinkList) > 0):
                            self.urlManager.addNewUrls(newLinkList)

                        # 将新的数据保存下来
                        if(newDataDict is not None):
                            self.newDataList.append(newDataDict)

                i += 1
                self.htmlDrawer.outPut(self.newDataList)
        except Exception as e:
            print(e)


if(__name__ == '__main__'):
    rootUrl = 'http://baike.baidu.com/view/5089421.htm'
    spider = Spider()
    spider.execute(rootUrl)
