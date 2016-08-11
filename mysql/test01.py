#!/usr/bin/python
# coding=utf-8
import MySQLdb
# 创建一个表
try:
    conn = MySQLdb.Connect(
        host='localhost',
        user='root',
        passwd='123456',
        port=3306,
        db='zhihuishu',
        charset='utf8'
    )
    cursor = conn.cursor()
    create_sql = """
    CREATE TABLE `zhs_cdn` (
    `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
    `cdn_total` int(11) NOT NULL DEFAULT '0' COMMENT '请求总数',
    `cdn_success` int(11) NOT NULL DEFAULT '0' COMMENT '成功总数',
    `cdn_1000` int(11) NOT NULL DEFAULT '0' COMMENT '超过1000毫秒的总数',
    `cdn_wifi` int(11) NOT NULL DEFAULT '0' COMMENT '超过1000毫秒的总数中wifi总数',
    `cdn_mobile` int(11) NOT NULL DEFAULT '0' COMMENT '超过1000毫秒的总数中mobile总数',
    `cdn_fail` int(11) NOT NULL DEFAULT '0' COMMENT '失败总数',
    `dateline` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '添加的时间',
    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=4432 DEFAULT CHARSET=utf8 COMMENT='cdn'
    """
    cursor.execute(create_sql)
    print(cursor.rowcount)
    # cursor.commit()
    cursor.close()
    conn.close()
except MySQLdb.Error,e:
    print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
