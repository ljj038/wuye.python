#!/urs/bin/python
# coding=utf-8
import redis


class UrlManager:
    def __init__(self):
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=11, encoding='utf-8')
        self.newUrl = 'newUrl'
        self.oldUrl = 'oldUrl'

    # has more url
    def hasMoreNewUrl(self):
        return self.redis.scard(self.newUrl) > 0

    # get one url
    def getOneNewUrl(self):
        newurl = self.redis.spop(self.newUrl)
        self.redis.sadd(self.oldUrl, newurl)
        return newurl

    # add one url
    def addOneNewUrl(self, newUrl):
        if (len(newUrl) > 0):
            if (not self.redis.sismember(self.newUrl, newUrl) and not self.redis.sismember(self.oldUrl, newUrl)):
                self.redis.sadd(self.newUrl, newUrl)

    # add muliti url
    def addMuliNewUrl(self, newList):
        if (len(newList) > 0):
            for i in newList:
                self.addOneNewUrl(i)
