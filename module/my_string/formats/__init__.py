#!/usr/bin/python
#coding=utf-8
#当在主程序中使用 from package import * 时，如果包中的 __init__.py 代码定义了一个 __all__ 的列表
#就会按照列表中给出的模块名进行导入
__all__ = ['echo', 'dump'];
