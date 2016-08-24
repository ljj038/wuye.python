#!/usr/bin/python
# coding=utf-8
import urlManager
import htmlLoader
import htmlParser

class MainSpider:
    def __init__(self):
        try:
            self.urlManager = urlManager.UrlManager()
            self.htmlLoader = htmlLoader.HtmlLoader()
            self.htmlParser = htmlParser.HtmlParser()
        except Exception as e:
            print e

    def execute(self, newUrl):
        # print newUrl
        try:
            self.urlManager.addOneNewUrl(newUrl)
            if(self.urlManager.hasMoreNewUrl() > 0):
                sContent = self.htmlLoader.down(newUrl)
                if(sContent is not None):
                    lLink = self.htmlParser.getLinkList(newUrl=newUrl, sContent=sContent)
                    print lLink
        except Exception as e:
            print(e)


if (__name__ == '__main__'):
    rootUrl = 'http://www.mp4ba.com/'
    test = MainSpider()
    test.execute(rootUrl)
