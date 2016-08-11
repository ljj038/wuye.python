#!/usr/bin/python
# coding=utf-8
import MySQLdb
import sys
# select
try:
    conn = MySQLdb.Connect(
        host='localhost',
        user='root',
        passwd='123456',
        port=3306,
        db='zhihuishu',
        charset='utf8'
    )
except MySQLdb.Error, e:
    log = "Mysql connect error %d: %s"%(e.args[0], e.args[1])
    sys.exit(log)

# 判断一个变量是否被定义
# if('conn' not in dir()):
#     sys.exit("222")

try:
    # 创建一个 cursor
    cursor = conn.cursor()

    sql = 'select * from zhs_area limit 10'
    cursor.execute(sql)
    # print(cursor.rowcount)
    # print(cursor.fetchone())
    # print(cursor.fetchmany(5))
    # print(cursor.fetchall())
    # 迭代
    # 默认返回的是元组
    for tp in cursor.fetchall():
        print("%s,%s,%s,%s"%(tp))
except MySQLdb.Error, e:
    log = "Mysql connect error %d: %s"%(e.args[0], e.args[1])
    sys.exit(log)
