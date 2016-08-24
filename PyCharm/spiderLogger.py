#!/usr/bin/python
# coding=utf-8
import logging
import datetime


class SpiderLogger:
    __sLogDir = 'log/'
    __sLogName = datetime.datetime.now().strftime('%Y%m%d') + '.log'
    __sLogerName = 'mp4baLogger'
    __objFormatter = logging.Formatter('%(asctime)s %(clientip)s-%(user)-8s %(name)s %(levelname)s-%(message)s')
    __objLogger = logging.getLogger(__sLogerName)
    __objLogger.setLevel(logging.DEBUG)
    __objFileHandler = logging.FileHandler(__sLogDir + __sLogName)
    __objFileHandler.setFormatter(__objFormatter)
    __objLogger.addHandler(__objFileHandler)

    @staticmethod
    def log(content=None, type_=None, d={}):
        if (content is None):
            return

        if (type_ is None):
            type_ = 'debug'

        type_ = type_.lower()

        if (len(d) == 0):
            d = {'clientip': '192.168.0.1', 'user': 'zhaoyingnan'}
        else:
            if (d.get('clientip', None) is None):
                d['clientip'] = '192.168.0.1'

            if (d.get('user', None) is None):
                d['user'] = 'zhaoyingnan'

        if (type_ == 'critical'):
            SpiderLogger.__objLogger.critical(content, extra=d)
        elif (type_ == 'error'):
            SpiderLogger.__objLogger.error(content, extra=d)
        elif (type_ == 'warning'):
            SpiderLogger.__objLogger.warning(content, extra=d)
        elif (type_ == 'info'):
            SpiderLogger.__objLogger.info(content, extra=d)
        else:
            SpiderLogger.__objLogger.debug(content, extra=d)
