#!/usr/bin/env python
# coding=utf-8
__author__ = 'zhaoyingnan'
import numpy

# 创建一个数组
a = numpy.arange(15)
print(a)  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
b = numpy.arange(0, 10)
print(b)  # [0 1 2 3 4 5 6 7 8 9]
c = numpy.arange(0, 20, 5)
print(c)  # [ 0  5 10 15]

str = '0123456789'
d = numpy.array(list(str))
print(d)  # ['0' '1' '2' '3' '4' '5' '6' '7' '8' '9']

# 随机
print(numpy.random.randint(10))  # 1<=n<10
print(numpy.random.randint(5, 10))  # 5<=n<10
print(numpy.random.randint(1, 10, 10))  # [2 4 2 3 6 3 6 4 4 5] 10个 1<=n<10的随机数
