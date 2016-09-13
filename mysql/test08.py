#!/usr/bin/env python
# coding=utf-8
__author__ = 'zhaoyingnan'
import MySQLdb

try:
    conn = MySQLdb.Connect(
        host='localhost',
        user='root',
        passwd='123456',
        port=3306,
        db='laravel',
        charset='utf8',
    )

    # 创建一个 cursor 结果集使用字典
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    # cursor = conn.cursor()

    sql = 'select * from student'
    cursor.execute(sql)
    result = cursor.fetchall()
    # for i in result:
    #     print i[1]
    # exit()
    for index, dt in enumerate(result):
        print dt['name']
        # print dt  # {'name': u'\u8d75\u82f1\u6960', 'age': 24, 'update_at': 0L, 'create_at': 0L, 'sex': 1, 'id': 1L}

        # for key, value in dict.iteritems(dt):
        #     print("%s=>%s" % (key, value)),  # 后面加","是为了不换行
except Exception as e:
    log = "Mysql connect error %d: %s" % (e.args[0], e.args[1])
    print log
