#!/usr/bin/python
#coding=utf-8
#Python的元组与列表类似，不同之处在于元组的元素不能修改
#元组使用小括号，列表使用方括号
#元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可
#如下实例：
tup1 = ('windows', 'linux');
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";
print tup1;
print tup2;
print tup3;

#创建空元组
tup4 = ();

#元组中只包含一个元素时，需要在元素后面添加逗号
tup4 = (5,);
print tup4;

#元组与字符串类似，下标索引从0开始，可以进行截取，组合等
#通过索引访问元组中的值
print tup1[0];#windows

#元组中的元素值是不允许修改的
#tup1[0] = 1;#TypeError: 'tuple' object does not support item assignment

#但我们可以对元组进行连接组合，如下实例:
tup6 = tup1 + tup2;
print tup6;#('windows', 'linux', 1, 2, 3, 4, 5)

#元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:
#del tup6[0];#TypeError: 'tuple' object doesn't support item deletion
del tup6;
#print tup6;#NameError: name 'tup6' is not defined

#迭代
for t in tup2:
    print t;

for t in range(len(tup2)):
    print tup2[t];

#切片
print tup2[2:];#(3, 4, 5)

#计算元组元素个数
print len(tup2);#5
#返回元组中元素最大值
print max(tup2);#5
#返回元组中元素最小值
print min(tup2);#1
#将列表转换为元组
list1 = ['apple','banana'];
tup7 = tuple(list1);
print tup7;#('apple', 'banana')
