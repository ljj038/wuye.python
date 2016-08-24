#!/usr/bin/python
# coding=utf-8
import urlManager
import htmlLoader
import htmlParser
from spiderLogger import SpiderLogger


class MainSpider:
    def __init__(self):
        try:
            self.urlManager = urlManager.UrlManager()
            self.htmlLoader = htmlLoader.HtmlLoader()
            self.htmlParser = htmlParser.HtmlParser()
        except Exception as e:
            SpiderLogger.log(e)

    def setStartUrl(self, sUrl):
        self.startUrl = sUrl

    def execute(self):
        try:
            sFirstPageUrl = 'http://www.mp4ba.com?page=1'
            sFirstPageContent = self.htmlLoader.down(sFirstPageUrl)
            iPage = self.htmlParser.getTotalPage(sFirstPageUrl, sFirstPageContent)
            if (iPage > 1):
                i = 1
                while 1:
                    if (i > iPage):
                        break

                    sPerPageUrl = 'http://www.mp4ba.com?page=%d' % i
                    sPerPageContent = self.htmlLoader.down(sPerPageUrl)
                    if (sPerPageContent is not None):
                        lLink = self.htmlParser.getLinkList(sPerPageUrl, sPerPageContent)
                        print len(lLink)
                    i += 1

        except Exception as e:
            SpiderLogger.log(e)


if (__name__ == '__main__'):
    rootUrl = 'http://www.mp4ba.com?page=1'
    test = MainSpider()
    test.execute()
