#!/usr/bin/env python
# coding=utf-8
__author__ = 'zhaoyingnan'
import numpy as np
import pandas as pd

# DataFrame is a 2-dimensional labeled data structure with columns of potentially different types


# build a DataFrame From dict of Series or dicts
s1 = pd.Series(data=2.1, index=['a', 'b', 'c', 'd'])
s2 = pd.Series(data=1.3, index=['a', 'b', 'c', 'd'])
s4 = pd.Series(data=4.5, index=['a', 'b', 'c', 'd'])
d = {'one': s1, 'two': s2, 'four': s4}

# The row and column labels can be accessed respectively by accessing the index and columns attributes
# index 和 columns 设置被访问的行和列
# index     <=>     row(行)
# columns   <=>     column(列)
d1 = pd.DataFrame(data=d, index=['a', 'b', 'c', 'd'], columns=['one', 'two', 'three', 'four'])
# print(d1)
#    one  two three  four
# a  2.1  1.3   NaN   4.5
# b  2.1  1.3   NaN   4.5
# c  2.1  1.3   NaN   4.5
# d  2.1  1.3   NaN   4.5


# build a DataFrame From a list of dicts
l = [{'x': 10.2, 'y': 13.7, 'z': 8.4}, {'x': 11.7, 'y': 8.6, 'z': 14.8}]
d2 = pd.DataFrame(data=l, index=['row1', 'row2'], columns=['x', 'y', 'z', 'm'])
# print(d2)
#          x     y     z   m
# row1  10.2  13.7   8.4 NaN
# row2  11.7   8.6  14.8 NaN

# Column selection, addition, deletion
# selection
d2['m'] = d2['y'] > 10
# print(d2)
#          x     y     z      m
# row1  10.2  13.7   8.4   True
# row2  11.7   8.6  14.8  False

# deletion
del (d2['m'])
# d2.pop('m')  # Columns can be deleted or popped like with a dict
# print(d2)
#          x     y     z
# row1  10.2  13.7   8.4
# row2  11.7   8.6  14.8

# addition
d2['m'] = d2['x'] + d2['y'] + d2['z']
# print(d2)
#          x     y     z     m
# row1  10.2  13.7   8.4  32.3
# row2  11.7   8.6  14.8  35.1

# describe()函数对于数据的快速统计汇总
# print(d2.describe())
#               x          y          z          m
# count   2.00000   2.000000   2.000000   2.000000
# mean   10.95000  11.150000  11.600000  33.700000
# std     1.06066   3.606245   4.525483   1.979899
# min    10.20000   8.600000   8.400000  32.300000
# 25%    10.57500   9.875000  10.000000  33.000000
# 50%    10.95000  11.150000  11.600000  33.700000
# 75%    11.32500  12.425000  13.200000  34.400000
# max    11.70000  13.700000  14.800000  35.100000

# 查看frame中头部的行
# print(d2.head(1))
#          x     y    z     m
# row1  10.2  13.7  8.4  32.3

# 查看frame中尾部的行
# print(d2.tail(1))
#          x    y     z     m
# row2  11.7  8.6  14.8  35.1
