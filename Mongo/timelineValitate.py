#!/usr/bin/python
# coding=utf-8
import pymongo
import datetime
import time

sDate = '1991-11-11 11:11:11'
iTimestamp = int(time.mktime(time.strptime(sDate, '%Y-%m-%d %H:%M:%S')))
print  iTimestamp
sUTCDate = datetime.datetime.utcfromtimestamp(iTimestamp)
# print  sUTCDate
dSchoolCount = {202002585: 0, 202002644: 0, 202002646: 0, 202002619: 0, 202002624: 4768, 202002627: 431, 202002611: 34,
                202002634: 195, 202002637: 1039, 202002605: 2269, 202002643: 1532, 202002588: 2, 202002602: 1250,
                202002595: 2934,
                202002626: 270, 202002630: 1888, 202002582: 1, 202002589: 14, 202002645: 230, 202002608: 1117,
                202002581: 7943, 202002629: 1777, 202002593: 1576, 202002590: 26, 202002604: 1861, 202002622: 595,
                202002606: 9206, 202002651: 51, 202002642: 3, 202002615: 245, 202002640: 44, 202002633: 79,
                202002610: 88, 202002578: 143, 202002597: 469, 202002635: 94, 202002592: 988, 202002623: 396,
                202002621: 13, 202002587: 5556, 202002620: 8654, 202002603: 859, 202002650: 82, 202002600: 1292,
                202002594: 942, 202002591: 2652, 202002596: 6, 202002583: 77, 202002609: 42, 202002599: 1055,
                202002649: 52, 202002607: 295, 202002586: 2939, 202002579: 761, 202002584: 117, 202002636: 5323,
                202002625: 252, 202002638: 49, 202002647: 182, 202002648: 5544, 202002612: 108, 202002616: 1070,
                202002628: 681, 202002613: 1631, 202002632: 121, 202002617: 1, 202002631: 288, 202002639: 482,
                202002614: 160, 202002618: 1457, 202002601: 4, 202002598: 360, 202002580: 149, 202002641: 55}

dSchoolCount2 = {202038169: 114, 202038198: 4706, 202038201: 431, 202038183: 34, 202038208: 195, 202038213: 1039,
                 202038177: 2271, 202038220: 1534, 202038156: 2, 202038174: 1261, 202038165: 2929, 202038200: 270,
                 202038204: 1899, 202038150: 1, 202038157: 14, 202038189: 406, 202038222: 237, 202038180: 1117,
                 202038149: 7950, 202038203: 1778, 202038163: 1576, 202038217: 492, 202038159: 26, 202038176: 1854,
                 202038196: 601, 202038178: 9210, 202038160: 51, 202038219: 3, 202038188: 245, 202038216: 44,
                 202038207: 79, 202038182: 88, 202038146: 143, 202038167: 469, 202038211: 94, 202038162: 988,
                 202038197: 396, 202038171: 2076, 202038195: 13, 202038158: 141, 202038155: 5656, 202038194: 8677,
                 202038209: 1288, 202038153: 0, 202038175: 859, 202038221: 0, 202038210: 10601, 202038187: 280,
                 202038227: 82, 202038172: 1292, 202038164: 945, 202038161: 2654, 202038166: 6, 202038151: 77,
                 202038181: 42, 202038170: 1055, 202038226: 52, 202038223: 0, 202038179: 295, 202038154: 2948,
                 202038147: 767, 202038152: 117, 202038212: 5330, 202038199: 252, 202038193: 0, 202038214: 49,
                 202038224: 182, 202038225: 5544, 202038184: 108, 202038190: 1070, 202038202: 691, 202038185: 1640,
                 202038206: 121, 202038191: 1, 202038205: 288, 202038215: 482, 202038186: 160, 202038192: 1459,
                 202038173: 4, 202038168: 360, 202038148: 149, 202038218: 56}

# 建立连接
objClient = pymongo.MongoClient("127.0.0.1", 20000)
# 设置操作的 database
objDB = objClient['timeline']
for key, value in dict.iteritems(dSchoolCount2):
    # 设置操作的集合 collection
    collection = 'zhs_timeline_%d' % (int(key) % 2000)
    iCount = objDB[collection].find({"deleted_time": sUTCDate, "school_id": key}).count()
    if (iCount != value):
        print(key, collection, iCount, value, 'fail')
    else:
        print(key, collection, iCount, value, 'ok')

