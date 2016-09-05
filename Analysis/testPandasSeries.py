#!/usr/bin/env python
# coding=utf-8
__author__ = 'zhaoyingnan'
import pandas as pd
import numpy as np

# Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.).
# np.nan (NaN (not a number))is the standard missing data marker used in pandas

# build a Series from a list
l = [1, 2, 3, 4, 5, 6, np.nan, 8, 9, 10]
i = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
s = pd.Series(data=l)
# print(s)
# 0     1.0
# 1     2.0
# 2     3.0
# 3     4.0
# 4     5.0
# 5     6.0
# 6     NaN
# 7     8.0
# 8     9.0
# 9    10.0

s = pd.Series(data=l, index=i)
# print(s)
# a     1.0
# b     2.0
# c     3.0
# d     4.0
# e     5.0
# f     6.0
# g     NaN
# h     8.0
# i     9.0
# j    10.0
# dtype: float64

# build a Series from a dict
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'h': np.nan, 'i': 5, 'g': 6}
s = pd.Series(data=d)
# print(s)
# a    1.0
# b    2.0
# c    3.0
# d    4.0
# g    6.0
# h    NaN
# i    5.0
# dtype: float64


# build a Series From scalar value If data is a scalar value, an index must be provided. The value will be repeated to match the length of index
s = pd.Series(2.2, index=i)
# print(s)
# a    2.2
# b    2.2
# c    2.2
# d    2.2
# e    2.2
# f    2.2
# g    2.2
# h    2.2
# i    2.2
# j    2.2
# dtype: float64

# Series can also have a name attribute
s = pd.Series(data=1.3, index=['a', 'b', 'c'], name='something')
# print(s.name)  # something

# You can rename a Series with the pandas.Series.rename() method
s3 = s.rename('myName')
# Note that s and s2 refer to different objects
# print(s3.name)  # myName


# A Series is like a fixed-size dict in that you can get and set values by index label:
# If a label is not contained, an exception is raised:
# print(s['z'])  # KeyError: 'z'
# Using the get method, a missing label will return None or specified default:
# print(s.get('z', np.nan))  # nan


s2 = pd.Series([1, 2, 3, 4])
# print(s2 + s2)
# 0    2
# 1    4
# 2    6
# 3    8
# dtype: int64

# Series operations
# print(s2 * 2)
# 0    2
# 1    4
# 2    6
# 3    8
# dtype: int64

# Series slice
# print(s2[1:3])
# 1    2
# 2    3
# dtype: int64
# print(s2[:-1])
# 0    1
# 1    2
# 2    3
# dtype: int64

# describe()函数对于数据的快速统计汇总
# print(s.describe())
# count    3.0
# mean     1.3
# std      0.0
# min      1.3
# 25%      1.3
# 50%      1.3
# 75%      1.3
# max      1.3

# 查看Series中头部的行
# print(s.head(1))
# a    1.3
# Name: something, dtype: float64
# 查看Series中尾部的行
# print(s.tail(2))
# b    1.3
# c    1.3
# Name: something, dtype: float64
