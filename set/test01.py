#!/usr/bin/python
#coding=utf-8
#set（集合）
#集合是一个无序不重复元素的集
#基本功能包括关系测试和消除重复元素
#集合对象还支持 union(联合)，intersection(交)，difference(差)和 sysmmetric difference(对称差集)等数学运算。

#创建一个空集合
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana'];#有重复的元素
fruits = set(basket);
print fruits;#set(['orange', 'pear', 'apple', 'banana'])

#对字符串去重
set1 = set('banana');
print set1;#set(['a', 'b', 'n'])
set2 = set('apple');
print set2;#set(['a', 'p', 'e', 'l'])

#判断指定一个元素是否在集合中
print 'apple' in fruits;#True

#交集，并集，差集，差集取反
print set1 - set2;#set(['b', 'n'])，差集，在set1但是不在set2中
print set2 - set1;#set(['p', 'e', 'l'])，差集，在set2但是不在set1中
print set1 | set2;#set(['a', 'p', 'b', 'e', 'l', 'n']),并集
print set1 & set2;#set(['a']),交集
print set1 ^ set2;#set(['b', 'e', 'l', 'n', 'p']),交集取反


#集合推导式
set3 = {x for x in 'abracadabra' if x not in 'abr'};
print set3;#set(['c', 'd'])
