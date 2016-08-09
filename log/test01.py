#!/usr/bin/python
# coding=utf-8
import logging
d = {'clientip': '192.168.0.1', 'user': 'zhaoyingnan'}

# 创建一个formater实例 用于设置输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 创建一个logger实例
myLogger = logging.getLogger('demoLogger')

# 设置级别
myLogger.setLevel(logging.DEBUG)
# logger 的可设置级别(
# CRITICAL 50
# ERROR   40
# WARNING 30
# INFO    20
# DEBUG   10
# NOTSET  0)


# 创建一个handler 用于写入日志文件
fileHandler = logging.FileHandler('demoLogger.log')

# 创建一个handler 用于屏幕输出
streamHandler = logging.StreamHandler()

# 为handler设置格式
fileHandler.setFormatter(formatter)
streamHandler.setFormatter(formatter)

# 为logger 实例添加handler 输出到日志文件
myLogger.addHandler(fileHandler)

# 为logger 实例再添加一个handler 在屏幕输出
myLogger.addHandler(streamHandler)

# 移除handler
# myLogger.removeHandler(streamHandler)

myLogger.debug('myLogger debug message', extra=d)
myLogger.info('myLogger info message', extra=d)
myLogger.warning('myLogger warning message', extra=d)
myLogger.error('myLogger error message', extra=d)
myLogger.critical('myLogger critical message', extra=d)

# 注意事项:
# 默认情况下python的logging模块将日志打印到了标准输出中
# 且只显示了大于等于WARNING级别的日志
# 这说明默认的日志级别设置为WARNING
# （日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET）
# 默认的日志格式为日志级别：Logger名称：用户输出消息
