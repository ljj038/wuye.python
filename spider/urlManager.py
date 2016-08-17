#!/usr/bin/python
# coding=utf-8
import redis


class urlManager:

    def __init__(self):
        try:
            self.conn = redis.StrictRedis(host='localhost', port=6379, db=0)
        except Exception as e:
            raise Exception(e)
        finally:
            pass

    def addNewUrl(self, url):
        try:
            if(url is None):
                return False
            if((not self.conn.sismember('newUrlSet', url)) and (not self.conn.sismember('oldUrlSet', url))):
                if(self.conn.sadd('newUrlSet', url) != 1):
                    raise Exception('urlManager.addNewUrl redis add fail')
        finally:
            pass

    def addNewUrls(self, urls):
        if(urls is None):
            return False

        for url in urls:
            self.addNewUrl(url)

        return True

    def hasNewUrl(self):
        return self.conn.scard('newUrlSet') != 0

    def getNewUrl(self):
        url = self.conn.spop('newUrlSet')
        self.conn.sadd('oldUrlSet', url)
        return url
