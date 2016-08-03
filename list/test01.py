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

#删除元素
list1 = ['a', 'b', 'c', 'd', 'e', 'f'];
print list1;#['a', 'b', 'c', 'd', 'e', 'f']
del list1[0];
print list1;#['b', 'c', 'd', 'e', 'f']

#列表重复
list2 = ['a'];
print list2 * 4;#['a', 'a', 'a', 'a']

#迭代
for w in list1:
    print w;

for index in range(len(list1)):
    print list1[index];

#list1.append('a');
#判断元素是否存在于列表中
if 'a' in list1:
    print 'a in list1';
else:
    print 'a not in list1';


#获取列表的最大/最小值
list3 = [1,2,3,4];
print max(list3);#4
print min(list3);#1
list4 = [6,7,8,9];
print max(list4);#9
print min(list4);#6


#在列表末尾追加
list3.append(10);
print list3;#[1, 2, 3, 4, 10]
list3.append([10,11,12]);
print list3;#[1, 2, 3, 4, 10, [10, 11, 12]]

#在列表的末尾一次性追加另一个列表中的多个值
list5 = ['a', 'b', 'c', 'd'];
list6 = [1];
list6.extend(list5);
print list6;#[1, 'a', 'b', 'c', 'd']

#统计每个元素在列表中出现的次数
i = 1;
while i<=3:
    list3.append(10);
    i += 1;

print list3;#[1, 2, 3, 4, 10, [10, 11, 12], 10, 10, 10]
print list3.count(10);#4

#从列表中找出某个值第一个匹配项的索引值
list7 = [1,2,3,1,2,3];
print list7.index(2);#1

#将对象插入列表,只是插入到指定的位置，索引会依次顺延
list7.insert(3,100);
print list7;#[1, 2, 3, 100, 1, 2, 3]

#移除列表中的某个值的第一个匹配项
list7.remove(1);
print list7;#[2, 3, 100, 1, 2, 3]

#移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print list7.pop(0);#2

#反转列表的元素
list7.reverse();
print list7;#[3, 2, 1, 100, 3]

#排序
list7.sort();
print list7;#[1, 2, 3, 3, 100]


#列表推导式
#列表推导式为从序列中创建列表提供了一个简单的方法
#普通的应用程序通过将一些操作应用于序列的每个成员并通过返回的元素创建列表，或者通过满足特定条件的元素创建子序列
squares = [];
for x in range(10):
    squares.append(x**2);
print squares;#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#采用下面的方式,可以达到同样的目的:
squares = [i**2 for i in range(10)];
print squares;#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = [];
for x in range(10):
    if(x%2 == 0):
        squares.append(x**2);
print squares;#[0, 4, 16, 36, 64]
#等同于下面
squares = [i**2 for i in range(10) if i%2==0]
print squares;#[0, 4, 16, 36, 64]
