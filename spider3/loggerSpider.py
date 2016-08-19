#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import datetime


class loggerSpider:
    # logDir
    logDir = 'log/'
    # logName
    logName = datetime.datetime.now().strftime('%Y%m%d') + '.log'
    # 实例一个 logger
    logger = logging.getLogger('spiderLogger')
    # 定义全局的 Formatter 实例 用于设置日志的格式
    __formatter = logging.Formatter('%(asctime)s %(clientip)s-%(user)-8s %(name)s %(levelname)s-%(message)s')

    # 实例一个 Handler
    fileHandler = logging.FileHandler(logDir + logName)

    # 设置级别
    logger.setLevel(logging.DEBUG)

    # 设置 Handler 格式
    fileHandler.setFormatter(__formatter)

    # 将 fileHandler 添加到 logger
    logger.addHandler(fileHandler)

    @staticmethod
    def log(content=None, type_=None, d={}):
        if(content is None):
            return

        if(type_ is None):
            type_ = 'debug'

        type_ = type_.lower()

        if(len(d) == 0):
            d = {'clientip': '192.168.0.1', 'user': 'zhaoyingnan'}
        else:
            if(d.get('clientip', None) is None):
                d['clientip'] = '192.168.0.1'

            if(d.get('user', None) is None):
                d['user'] = 'zhaoyingnan'

        if(type_ == 'critical'):
            loggerSpider.logger.critical(content, extra=d)
        elif(type_ == 'error'):
            loggerSpider.logger.error(content, extra=d)
        elif(type_ == 'warning'):
            loggerSpider.logger.warning(content, extra=d)
        elif(type_ == 'info'):
            loggerSpider.logger.info(content, extra=d)
        else:
            loggerSpider.logger.debug(content, extra=d)
