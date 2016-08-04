#!/usr/bin/python
#coding=utf-8
#dict(字典)，在某些语言中可能称为 联合内存 (associative memories) 或 联合数组 (associative arrays)
#序列是以连续的整数为索引，与此不同的是，字典以 关键字 为索引，关键字可以是任意不可变类型，通常用字符串或数值

#创建一个空字典
tel = {};

#初始化
tel = {'jack':13303028786};
print tel;#{'jack': 13303028786}

#其他方式创建字典
tel1 = dict([('a',1),('b',2)]);
print tel1;#{'a': 1, 'b': 2}

tel2 = dict(sape=4139, guido=4127, jack=4098);
print tel2;#{'sape': 4139, 'jack': 4098, 'guido': 4127}


#访问字典中的值
print tel['jack'];#13303028786


#修改字典里的值
tel['jack'] = 15932279586;
print tel['jack'];#15932279586


#新增/删除
tel['zhao'] = 15313032527;
print tel;#{'zhao': 15313032527, 'jack': 15932279586}
del tel['jack'];
print tel;#{'zhao': 15313032527}


#计算字典元素的个数
print len(tel);#1


#输出字典可打印的字符串表示
print str(tel);#{'zhao': 15313032527}


#清空字典内所有的元素,只是清空，并不是删除了tel
tel.clear();
print tel;#{}


#复制字典，并赋值给另一个变量
price = {'apple':3.45, 'banana':5.5};
dict1 = price.copy();
print dict1;#{'apple': 3.45, 'banana': 5.5}


#创建一个字典，以seq列表的元素为键，也可指定键对应的值
seq1 = ['a','b','c'];
dict2 = dict.fromkeys(seq1);
print dict2;#{'a': None, 'c': None, 'b': None}
dict2 = dict.fromkeys(seq1, 100);
print dict2;#{'a': 100, 'c': 100, 'b': 100}

seq2 = ('d', 'e', 'f');
dict3 = dict.fromkeys(seq2);
print dict3;#{'e': None, 'd': None, 'f': None}
dict3 = dict.fromkeys(seq2, 200);
print dict3;#{'e': 200, 'd': 200, 'f': 200}


#返回指定键的值，如果值不在字典中返回default值
#dict.get(key, default=None) 函数返回指定键的值，如果值不在字典中返回默认值
dict4 = {'apple':3.45, 'banana':5.5};
if(dict4.get('apple',0) != 0):
    print 'apple price is ',dict4['apple'];
else:
    print 'can not find apple\'s price';


#判断指定的键是否在字典中,如果键在字典dict里返回true，否则返回false
print dict4.has_key('apple');#True


#以列表返回可遍历的(键, 值) 元组数组
print dict4.items();#[('apple', 3.45), ('banana', 5.5)]


#以列表返回一个字典所有的键
print dict4.keys();#['apple', 'banana']


#以列表返回字典中的所有值
print dict4.values();#[3.45, 5.5]


#把字典dict2的键/值对更新到dict里,已存在的键会被修改值，不存在的键会被插入
print dict4;#{'apple': 3.45, 'banana': 5.5}
dict5 = {'apple':3, 'banana':5, 'bb':10};
dict4.update(dict5);
print dict4;#{'apple': 3, 'bb': 10, 'banana': 5}


#判断一个键在字典中是否存在，若不存在，则添加该键，并设置为default指定的值
#setdefault(key, default=None)
print dict5;#{'apple': 3, 'bb': 10, 'banana': 5}
dict5.setdefault('cc', 100);
print dict5;#{'cc': 100, 'apple': 3, 'bb': 10, 'banana': 5}
