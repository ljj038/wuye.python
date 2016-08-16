#!/usr/bin/python
# coding=utf-8
# python 正则抓取图片
import urllib2
import re
import os
urlSet = ('http://car.autohome.com.cn/pic/brand-49.html',
          'http://car.autohome.com.cn/pic/series/874.html#pvareaid=2042214')
for url in urlSet:
    content = urllib2.urlopen(url).read()
    pattern = re.compile(r'<img[\s\w\d_"\'=]*src="([^"]+\.(?:jpg|png|gif|jpeg))"', re.I)
    imgList = pattern.findall(content)
    imgSet = set(imgList)
    for url in imgSet:
        print(url)
        f = open('img/' + os.path.basename(url), 'w')
        imgContent = urllib2.urlopen(url).read()
        f.write(imgContent)
        f.close()
