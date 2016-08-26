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

lSchool = [202002585, 202002644, 202002646, 202002619, 202002624, 202002627, 202002611, 202002634, 202002637, 202002605,
           202002643, 202002588, 202002602, 202002595, 202002626, 202002630, 202002582, 202002589, 202002645,
           202002608, 202002581, 202002629, 202002593, 202002590, 202002604, 202002622, 202002606, 202002651, 202002642,
           202002615, 202002640, 202002633, 202002610, 202002578, 202002597, 202002635, 202002592, 202002623,
           202002621, 202002587, 202002620, 202002603, 202002650, 202002600, 202002594, 202002591, 202002596, 202002583,
           202002609, 202002599, 202002649, 202002607, 202002586, 202002579, 202002584, 202002636, 202002625,
           202002638, 202002647, 202002648, 202002612, 202002616, 202002628, 202002613, 202002632, 202002617, 202002631,
           202002639, 202002614, 202002618, 202002601, 202002598, 202002580, 202002641]

# 建立连接
objClient = pymongo.MongoClient("114.55.104.39", 27017)
# 设置操作的 database
objDB = objClient['timeline']
for i in lSchool:
    # 设置操作的集合 collection
    collection = 'zhs_timeline_%d' % (int(i) % 2000)
    print(i, collection, objDB[collection].find({"deleted_time": sUTCDate, "school_id": i}).count())

# 插入 Mongo
db = objClient['deepin']
print(db['test1'].insert({"aaaa": sUTCDate}))  # 插入一个UTC时间(python不会自动转化)


# find
objCursor = db['test1'].find()
for data in objCursor:
    print data