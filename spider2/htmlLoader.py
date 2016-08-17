#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2


class htmlLoader:
    # 获取url的内容
    def urlLoad(self, url):
        response = urllib2.urlopen(url)
        code = response.getcode()
        content = None
        if(code != 200):
            print("[%s] get content fail" % (url))
        else:
            content = response.read()
            return content
