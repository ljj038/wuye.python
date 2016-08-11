#!/usr/bin/python
# coding=utf-8
import MySQLdb
import sys
# select
# 由于 cursor.execute(sql) 默认返回的是元组 输出不方便 做一下修改即可
try:
    conn = MySQLdb.Connect(
        host='localhost',
        user='root',
        passwd='123456',
        port=3306,
        db='zhihuishu',
        charset='utf8',
    )
except MySQLdb.Error, e:
    log = "Mysql connect error %d: %s"%(e.args[0], e.args[1])
    sys.exit(log)

try:
    # 创建一个 cursor 结果集使用字典
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)

    sql = 'select * from zhs_area limit 10'
    cursor.execute(sql)
    result = cursor.fetchall()
    for index,dt in enumerate(result):
        for key,value in dict.iteritems(dt):
            print("%s=>%s"%(key, value)),  # 后面加","是为了不换行

        print  # 打印一个空行
except MySQLdb.Error, e:
    log = "Mysql connect error %d: %s"%(e.args[0], e.args[1])
    sys.exit(log)
