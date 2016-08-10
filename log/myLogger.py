#!/usr/bin/python
# coding=utf-8
import os
import logging
import datetime


class MyLogger:
    """MyLogger class"""
    # 定义全局的 Formatter 实例 用于设置日志的格式
    formatter = logging.Formatter('%(asctime)s %(clientip)s-%(user)-8s %(name)s %(levelname)s-%(message)s')

    def __init__(self, loggerName):
        # 创建一个 logger 实例
        self.logger = logging.getLogger(loggerName)
        # 设置默认级别
        self.logger.setLevel(logging.DEBUG)
        # 设置默认的日志保存目录
        self.dirName = '/tmp/demoLogger/'
        self.setLogDir(self.dirName)
        # 设置默认的日志文件
        self.logName = datetime.datetime.now().strftime('%Y%m%d') + '.log'

    # 设置保存日志的文件目录
    def setLogDir(self, dirName):
        if(dirName == ''):
            return False

        if(not os.path.isdir(dirName)):
            os.makedirs(dirName)

        self.dirName = dirName
        return True

    # 获取保存日志的目录
    def getLogDir(self):
        return self.dirName

    # 设置日志文件名
    def setLogName(self, logName):
        if(logName == ''):
            return False

        self.logName = logName
        return True

    # 获取日志文件名
    def getLogName(self):
        return self.logName

    # 添加 handler
    def addHangler(self, type=1):
        if(type == 1):
            # 创建一个 handler 用于写入文件日志
            fileHandler = logging.FileHandler(self.dirName + self.logName)
            # 设置格式
            fileHandler.setFormatter(MyLogger.formatter)
            # 添加到 logger
            self.logger.addHandler(fileHandler)
        elif(type == 2):
            # 创建一个 handler 用于屏幕输出
            streamHandler = logging.StreamHandler()
            # 设置格式
            streamHandler.setFormatter(MyLogger.formatter)
            # 添加到 logger
            self.logger.addHandler(streamHandler)
        else:
            return False

    # 记录log
    def log(self, level=10, levelString='info', message='test log', d={}):
        levelString = levelString.lower()
        if(level == 50 or levelString == 'critical'):
            self.logger.critical(message, extra=d)
        elif(level == 40 or levelString == 'error'):
            self.logger.error(message, extra=d)
        elif(level == 30 or levelString == 'warning'):
            self.logger.warning(message, extra=d)
        elif(level == 20 or levelString == 'info'):
            self.logger.info(message, extra=d)
        else:
            self.logger.debug(message, extra=d)

# demo

d = {'clientip': '192.168.0.1', 'user': 'zhaoyingnan'}
test = MyLogger('demoLogger')
test.addHangler(1)
test.addHangler(2)
test.log(level=0, levelString='error', message='myLogger debug message', d=d)
