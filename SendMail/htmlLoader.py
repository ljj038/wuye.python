#!/usr/bin/env python
# coding=utf-8
__author__ = 'zhaoyingnan'
import urllib
import urllib2
import chardet


class HtmlLoader:
    def urlLoad(self, sUrl):
        try:
            sContent = None
            dictHeaders = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Charset': 'utf-8',
                'Referer': 'https://www.baidu.com/?tn=92765401_hao_pg',
                'Accept-Language': 'zh-CN,zh;q=0.8',
            }
            dictData = {}
            sData = urllib.urlencode(dictData)
            Request = urllib2.Request(url=sUrl, data=sData, headers=dictHeaders)
            ProxyHandler = urllib2.ProxyHandler({})
            Opener = urllib2.build_opener(ProxyHandler)
            urllib2.install_opener(Opener)
            Response = Opener.open(Request)
            iCode = Response.getcode()
            if (iCode == 200):
                sContent = Response.read()

            if (sContent is not None):
                # print(chardet.detect(sContent))
                encoding = chardet.detect(sContent)
                if (encoding['encoding'].startswith("GB")):
                    sContent = sContent.decode("GBK")
            return sContent
        except Exception as e:
            print(e)
        finally:
            pass
