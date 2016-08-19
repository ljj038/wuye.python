#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb
from loggerSpider import loggerSpider


class dataHandler:
    def __init__(self):
        try:
            self.conn = MySQLdb.Connect(
                host='localhost',
                user='root',
                passwd='123456',
                port=3306,
                db='spider',
                charset='utf8',
            )

            self.conn.autocommit(False)
        except MySQLdb.Error as e:
            loggerSpider.log("Mysql connect error %d: %s" % (e.args[0], e.args[1]))

    def insert(self, newDataDict):
        newDataDict['title'] = newDataDict['title'].encode('utf-8')
        newDataDict['content'] = newDataDict['content'].encode('utf-8')
        sql = "insert into spider_article (`title`, `content`)values('%s', '%s')" % (MySQLdb.escape_string(newDataDict['title']), MySQLdb.escape_string(newDataDict['content']))
        # loggerSpider.log(sql)
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()
