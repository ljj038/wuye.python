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
            dHeader = {
                'User-Agent': 'Mozilla/50 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36'
            }

            # Request Object
            objRequest = urllib2.Request(url=newUrl, data=sData, headers=dHeader)

            # Handler Object
            objProxy = urllib2.ProxyHandler({})

            # Bulid & install
            opener = urllib2.build_opener(objProxy)
            urllib2.install_opener(opener)

            objResponse = opener.open(objRequest, timeout=100)
            iCode = objResponse.getcode()
            if (iCode == 200):
                content = objResponse.read()
            else:
                SpiderLogger.log('down html code fail[%s]' % newUrl)

        finally:
            return content

    def ukDown(self, sUkUrl, sFileName):
        dData = {}
        sData = urllib.urlencode(dData)
        dHeader = {}
        objRequest = urllib2.Request(url=sUkUrl, data=sData, headers=dHeader)
        objProxy = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(objProxy)
        urllib2.install_opener(opener)
        objResponse = opener.open(objRequest, timeout=150)
        iCode = objResponse.getcode()
        if (iCode == 200):
            content = objResponse.read()
            f = open('uk/%s.torrent' % sFileName[:sFileName.find('-')], 'w')
            f.write(content)
            f.close()
        else:
            SpiderLogger.log('down uk fail[%s]' % sUkUrl)
