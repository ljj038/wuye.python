#!/usr/bin/python
# coding=utf-8
import os
import datetime
import logging

# 准备日志的目录以及文件名
if(not os.path.isdir('./logdir')):
    os.makedirs('./logdir')
today = datetime.datetime.now().strftime('%Y%m%d') + '.log'

d = {'clientip': '192.168.10.1', 'user': 'zhaoyingnan'}
# 创建一个 logger 实例
myLogger = logging.getLogger('loggerDemo')

# 设置级别
myLogger.setLevel(logging.DEBUG)

# 创建一个 list 存储 handler
handlerList = []

# 创建一个 handler 用于写入文件日志
fileHandler = logging.FileHandler('./logdir/' + today)
handlerList.append(fileHandler)

# 再创建一个 handler 用于屏幕输出
streamHandler = logging.StreamHandler()
handlerList.append(streamHandler)

# 创建一个 formatter 实例 用于设置输出格式
formatter = logging.Formatter('%(asctime)s %(clientip)s-%(user)-8s %(name)s %(levelname)s-%(message)s')

# 为每个 handler 设置格式 并添加到 logger 实例中
for handler in handlerList:
    handler.setFormatter(formatter)
    myLogger.addHandler(handler)

# 测试
myLogger.debug('myLogger debug message', extra=d)
myLogger.info('myLogger info message', extra=d)
myLogger.warning('myLogger warning message', extra=d)
myLogger.error('myLogger error message', extra=d)
myLogger.critical('myLogger critical message', extra=d)
