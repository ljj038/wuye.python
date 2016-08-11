#!/usr/bin/python
# coding=utf-8
import MySQLdb
import sys
import os
import logging


class TransferMoney:
    """python mysql 的增删改查 以及事务的支持 并加入 logging"""

    # 定义全局的 Formatter 实例 用于设置日志的格式
    formatter = logging.Formatter('%(asctime)s %(clientip)s-%(user)-8s %(name)s %(levelname)s-%(message)s')
    d = {'clientip': '192.168.0.1', 'user': 'zhaoyingnan'}

    def __init__(self, conn):
        self.conn = conn
        self.logger = logging.getLogger('transferLogger')
        self.logger.setLevel(logging.DEBUG)
        if(not os.path.isdir("./log")):
            os.makedirs("./log")
        fileHandler = logging.FileHandler("./log/transfer.log")
        fileHandler.setFormatter(TransferMoney.formatter)
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(TransferMoney.formatter)
        self.logger.addHandler(fileHandler)
        self.logger.addHandler(streamHandler)


    def transfer(self, source_acctid, target_acctid, money):
        try:
            # 检测这两个用户是否存在
            self.checkAcctidAvailable(source_acctid)
            self.checkAcctidAvailable(target_acctid)
            # 检测付款人是否有足够的钱
            self.checkHasEnoughMoney(source_acctid, money)
            # 减去付款人的钱
            self.reduceMoney(source_acctid, money)
            # 增加收款人的钱
            self.addMoney(target_acctid, money)
            self.conn.commit()
            log = "%s已成功向%s转账%s元" % (source_acctid, target_acctid, money)
            self.logger.info(log, extra=TransferMoney.d)
        except Exception as e:
            self.logger.error(str(e), extra=TransferMoney.d)
        finally:
            self.conn.close()

    # 检测用户是否存在
    def checkAcctidAvailable(self, acctid):
        cursor = self.conn.cursor()
        try:
            sql = "select id from zhs_user where id = %s limit 1" % (acctid)
            self.logger.debug("checkAcctidAvailable " + sql, extra=TransferMoney.d)
            cursor.execute(sql)
            row = cursor.fetchall()
            if(len(row) != 1):
                raise Exception("%s 未找到该用户" % (acctid))
        finally:
            cursor.close()

    # 检测用户是否有足够的资金
    def checkHasEnoughMoney(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "select * from zhs_account where acctid = %s and money >= %s limit 1" % (acctid, money)
            self.logger.debug("checkHasEnoughMoney " + sql, extra=TransferMoney.d)
            cursor.execute(sql)
            row = cursor.fetchall()
            if(len(row) != 1):
                raise Exception("%s 该用户没有足够的资金(%s)" % (acctid, money))
        finally:
            cursor.close()

    # 减去付款人的钱
    def reduceMoney(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "update zhs_account set money=money-%s where acctid = %s" % (money, acctid)
            self.logger.debug("reduceMoney " + sql, extra=TransferMoney.d)
            cursor.execute(sql)
            if(cursor.rowcount != 1):
                raise Exception("%s 账号减款失败" % (acctid))
        finally:
            cursor.close()

    # 加上收款人的钱
    def addMoney(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "update zhs_account set money=money+%s where acctid = %s" % (money, acctid)
            self.logger.debug("reduceMoney " + sql, extra=TransferMoney.d)
            cursor.execute(sql)
            if(cursor.rowcount != 1):
                raise Exception("%s 账号加款失败" % (acctid))
        finally:
            cursor.close()

if(__name__ == "__main__"):
    source_acctid = 328
    target_acctid = 327
    money = 500
    try:
        conn = MySQLdb.Connect(
            host='localhost',
            user='root',
            passwd='123456',
            port=3306,
            db='zhihuishu',
            charset='utf8',
        )

        tr_money = TransferMoney(conn)
        tr_money.transfer(source_acctid, target_acctid, money)

        # 关闭自动提交
        conn.autocommit(False)
    except MySQLdb.Error as e:
        log = "Mysql connect error %d: %s" % (e.args[0], e.args[1])
        sys.exit(log)
