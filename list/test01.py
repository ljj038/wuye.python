#!/usr/bin/python
#coding=utf-8
#列表

#列表的元素不必是同一类型
squares = [1,2.1,3,'apple','banana', '楠哥'];
print squares;#[1, 2.1, 3, 'apple', 'banana', '\xe6\xa5\xa0\xe5\x93\xa5']

#列表的检索
print squares[0];#1
print squares[-1];#楠哥

#列表切片
squares = squares[0:3];
print squares;#[1, 2.1, 3]

#列表支持这样的操作
squares = squares + [100,101];
print squares;#[1, 2.1, 3, 100, 101]

#修改列表的元素
squares[0] = 'hello';
print squares;#['hello', 2.1, 3, 100, 101]

#向列表追加元素
squares.append('a');
print squares;#['hello', 2.1, 3, 100, 101, 'a']

#列表切片也可以被赋值，获取清空它
squares[0:3] = ['1a','2b','3c'];
print squares;#['1a', '2b', '3c', 100, 101, 'a']
squares[0:-2] = [];
print squares;#[101, 'a']
squares[:] = [];
print squares;#[]

#获取列表的长度
squares.append(101);
squares.append(102);
print len(squares);#2
