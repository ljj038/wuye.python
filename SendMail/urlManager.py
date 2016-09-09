#!/usr/bin/env python
# coding=utf-8
__author__ = 'zhaoyingnan'
import redis


class UrlManager:
    def __init__(self):
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)
        self.newUrlKey = "new-email-url"
        self.oldUrlKey = "old-email-url"

    def isExixts(self, sUrl):
        if ((self.redis.sismember(self.newUrlKey, sUrl)) or (self.redis.sismember(self.oldUrlKey, sUrl))):
            return True
        return False

    def insert(self, iType, sUrl):
        if (iType == 1):
            sKey = self.newUrlKey
        else:
            sKey = self.oldUrlKey
        return self.redis.sadd(sKey, sUrl)
