#!/usr/bin/python
# coding=utf-8
import urllib2
import urllib
from spiderLogger import SpiderLogger


class HtmlLoader:
    def down(self, newUrl):
        try:
            content = None
            dData = {}
            sData = urllib.urlencode(dData)
            dHeader = {}

            # Request Object
            objRequest = urllib2.Request(url=newUrl, data=sData, headers=dHeader)

            # Handler Object
            objProxy = urllib2.ProxyHandler({})

            # Bulid & install
            opener = urllib2.build_opener(objProxy)
            urllib2.install_opener(opener)

            objResponse = opener.open(objRequest, timeout=10)
            iCode = objResponse.getcode()
            if (iCode == 200):
                content = objResponse.read()
            else:
                SpiderLogger.log('down html code fail[%s]' % newUrl)

        finally:
            return content
