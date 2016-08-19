#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import urllib
from loggerSpider import loggerSpider


class htmlLoader:
    def __init__(self):
        pass

    def htmlDown(self, newUrl):
        try:
            content = None
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Referer': 'http://blog.jobbole.com/',
                'Accept-Language': 'zh-CN,zh;q=0.8'
            }
            data = {}
            data = urllib.urlencode(data)

            # request
            request = urllib2.Request(newUrl, data=data, headers=headers)

            # proxy
            # proxy_handler = urllib2.ProxyHandler({"http" : 'http://192.168.0.101:3128'})
            proxy_handler = urllib2.ProxyHandler({})

            # build opener
            opener = urllib2.build_opener(proxy_handler)

            # install opener
            urllib2.install_opener(opener)

            # response
            response = opener.open(request)

            # get code
            code = response.getcode()

            if(code != 200):
                return content

            content = response.read()
            if(content is None):
                loggerSpider.log('content is None [%s]' % (newUrl))
                return content

        finally:
            return content
