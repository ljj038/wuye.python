#!/usr/bin/python
# -*- coding: utf-8 -*-
import redis
from loggerSpider import loggerSpider


class urlManager:
    newUrlSetName = 'newUrl'
    oldUrlSetName = 'oldUrl'

    def __init__(self):
        self.conn = redis.StrictRedis(host='localhost', port=6379, db=10)
        if(self.conn is None):
            raise Exception('redis can not connect')

        self.conn.srem(urlManager.newUrlSetName, 'http://python.jobbole.com/')
        self.conn.srem(urlManager.oldUrlSetName, 'http://python.jobbole.com/')

    # 获取一个url
    def getOneUrl(self):
        newUrl = self.conn.spop(urlManager.newUrlSetName)
        if(newUrl is not None):
            self.conn.sadd(urlManager.oldUrlSetName, newUrl)

        return newUrl

    # 是否有更多
    def hasMoreUrls(self):
        return self.conn.scard(urlManager.newUrlSetName)

    # 添加一个url
    def addOneUrl(self, newUrl):
        if(newUrl is None):
            loggerSpider.log('newUrl is None')
            return

        if((not self.conn.sismember(self.newUrlSetName, newUrl)) and (not self.conn.sismember(self.oldUrlSetName, newUrl))):
            if(self.conn.sadd(self.newUrlSetName, newUrl) != 1):
                loggerSpider.log('newUrl add redis fail [%s]' % (newUrl))
            else:
                pass
        else:
            loggerSpider.log('newUrl is exists [%s]' % (newUrl))

    # 批量添加url
    def addUrls(self, newUrlList):
        if(len(newUrlList) != 0):
            for newUrl in newUrlList:
                self.addOneUrl(newUrl)
