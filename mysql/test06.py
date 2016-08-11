#!/usr/bin/python
# coding=utf-8
import MySQLdb
import sys
# update
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

    sql = "update zhs_cdn set cdn_mobile = 200 where id = 4439"
    n = cursor.execute(sql)
    print(n)  # 返回影响行数
    print(cursor.rowcount)  # 也可以这样获取影响行数
    # 提交
    conn.commit()
except MySQLdb.Error, e:
    conn.rollback()
    log = "Mysql connect error %d: %s"%(e.args[0], e.args[1])
    sys.exit(log)
