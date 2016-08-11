#!/usr/bin/python
# coding=utf-8
import MySQLdb
import sys
# insert
try:
    conn = MySQLdb.Connect(
        host='localhost',
        user='root',
        passwd='123456',
        port=3306,
        db='zhihuishu',
        charset='utf8',
    )

    # 关闭自动提交
    conn.autocommit(False)
except MySQLdb.Error, e:
    log = "Mysql connect error %d: %s"%(e.args[0], e.args[1])
    sys.exit(log)

try:
    cursor = conn.cursor()

    # 插入一行 start
    sql = "insert into zhs_cdn(cdn_total, cdn_success, cdn_1000, cdn_wifi, cdn_mobile, cdn_fail) values(0,0,0,0,0,0)"
    n = cursor.execute(sql)
    print(n)  # 返回影响行数
    print(cursor.rowcount)  # 也可以这样获取影响行数
    # 提交
    conn.commit()
    # 插入一行 end

    # 插入多行 start
    # sql = "insert into zhs_cdn(cdn_total, cdn_success, cdn_1000, cdn_wifi, cdn_mobile, cdn_fail) values(%s, %s, %s, %s, %s, %s)"
    # params = (
    #     (1, 2, 3, 4, 5, 6),
    #     (7, 8, 9, 10, 11, 12),
    #     (13, 14, 15, 16, 17, 18),
    #     (19, 20, 21, 22, 23, 24),
    # )
    # n = cursor.executemany(sql,params)
    # print(n)  # 返回影响行数
    # print(cursor.rowcount)  # 也可以这样获取影响行数
    # 插入多行 end

    # 提交
    # conn.commit()
except MySQLdb.Error, e:
    conn.rollback()
    log = "Mysql connect error %d: %s"%(e.args[0], e.args[1])
    sys.exit(log)
