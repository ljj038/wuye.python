#!/usr/bin/python
# coding=utf-8
import urllib2


class downLoader:
    def getContent(self, url):
        try:
            if(url is None):
                raise Exception('downLoader.getContent url is None')
            response = urllib2.urlopen(url)
            code = response.getcode()
            if(code != 200):
                raise Exception('downLoader.getContent response code is %s' % (code))
            return response.read()
        finally:
            pass
