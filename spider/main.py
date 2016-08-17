#!/usr/bin/python
# coding=utf-8
import urlManager
import downLoader
import htmlParser
import htmlOuter
import traceback


class Spi_main:
    def __init__(self):
        self.urlManager = urlManager.urlManager()
        self.downLoader = downLoader.downLoader()
        self.htmlParser = htmlParser.htmlParser()
        self.htmlOuter = htmlOuter.htmlOuter()
        self.dataList = []

    def execute(self, rootUrl):
        try:
            self.urlManager.addNewUrl(rootUrl)
            i = 1
            while(True):
                if(i == 100):
                    break

                if(self.urlManager.hasNewUrl()):
                    newUrl = self.urlManager.getNewUrl()
                    htmlContent = self.downLoader.getContent(newUrl)
                    newUrlSet, data = self.htmlParser.parse(newUrl, htmlContent)
                    self.urlManager.addNewUrls(newUrlSet)
                    if(data is not None):
                        self.dataList.append(data)
                else:
                    break
                i += 1

            self.htmlOuter.outPut(self.dataList)
        except Exception as e:
            print("error %s" % (e))
            print(traceback.print_exc())

if(__name__ == '__main__'):
    rootUrl = 'http://baike.baidu.com/view/48530.htm'
    spi = Spi_main()
    spi.execute(rootUrl)
