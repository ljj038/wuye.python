#!/usr/bin/python
# coding=utf-8
import pymongo
import datetime
import time

# 定义一个日期
sDate = '1991-11-11 11:11:11'
# 将一个日期转换为时间戳
iTimestamp = int(time.mktime(time.strptime(sDate, '%Y-%m-%d %H:%M:%S')))
print(iTimestamp)  # 689829071

# 将时间戳转换成指定的日期格式
setDate = time.localtime(iTimestamp)  # 先将时间戳转换为一个时间的元组
sDate = time.strftime("%Y-%m-%d %H:%M:%S", setDate)
print(sDate)  # 1991-11-11 11:11:11

# 将时间戳转换成UTC日期格式
sUTCDate = datetime.datetime.utcfromtimestamp(689829071)
print(sUTCDate)  # 1991-11-11 03:11:11

# 建立连接
objClient = pymongo.MongoClient("114.55.104.39", 27017)
# 设置操作的 database
objDB = objClient['timeline']

# 插入 Mongo
db = objClient['deepin']
print(db['test1'].insert({"aaaa": sUTCDate}))  # 插入一个UTC时间(python不会自动转化)

# find
objCursor = db['test1'].find()
for data in objCursor:
    print data
