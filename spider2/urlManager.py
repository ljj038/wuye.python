#!/usr/bin/python
# -*- coding: utf-8 -*-
import redis


class urlManager:
    """urlManager by redis"""
    def __init__(self):
        self.__newUrlSetName = 'newUrlSet'  # 存储未被处理的url
        self.__oldUrlSetName = 'oldUrlSet'  # 存储已被处理的url

        # redis
        try:
            self.__redis = redis.StrictRedis(host='localhost', port=6379, db=1)
            self.__redis.delete(self.__newUrlSetName)
            self.__redis.delete(self.__oldUrlSetName)
        except Exception as e:
            print(e)

    # 判断是否有更多的url
    def hasMoreUrl(self):
        return self.__redis.scard(self.__newUrlSetName)

    # 向 set 集合中添加新的url
    def addNewUrl(self, newUrl):
        if(newUrl is None):
            print("url is None")
            return

        if(
            (not self.__redis.sismember(self.__newUrlSetName, newUrl)) and
            (not self.__redis.sismember(self.__oldUrlSetName, newUrl))
        ):
            self.__redis.sadd(self.__newUrlSetName, newUrl)
        else:
            print("[%s] is exists" % (newUrl))

    # 批量添加新的url
    def addNewUrls(self, newUrlList):
        if(newUrlList is None):
            print("newUrlList is None")
            return
        for url in newUrlList:
            self.addNewUrl(url)

    # 获取一个新的url
    def getOneUrl(self):
        newUrl = self.__redis.spop(self.__newUrlSetName)
        self.__redis.sadd(self.__oldUrlSetName, newUrl)
        return newUrl
