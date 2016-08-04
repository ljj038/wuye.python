#!/usr/bin/python
#coding=utf-8
#遍历
#在序列中循环时，索引位置和对应值可以使用 enumerate() 函数同时得到:
questions = ['name', 'quest', 'favorite color'];
for index,value in enumerate(questions):
    print 'index=>',index,' value=>',value;
#index=> 0  value=> name
#index=> 1  value=> quest
#index=> 2  value=> favorite color

print;
#排序后，遍历
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for index,value in enumerate(sorted(basket)):#sorted并不会修改basket的值
    print 'index=>',index,' value=>',value;
#index=> 0  value=> apple
#index=> 1  value=> apple
#index=> 2  value=> banana
#index=> 3  value=> orange
#index=> 4  value=> orange
#index=> 5  value=> pear

print;

#反转后，遍历
num = range(11);
print num;#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index,value in enumerate(reversed(num)):
    print 'index=>',index,' value=>',value;
#index=> 0  value=> 10
#index=> 1  value=> 9
#index=> 2  value=> 8
#index=> 3  value=> 7
#index=> 4  value=> 6
#index=> 5  value=> 5
#index=> 6  value=> 4
#index=> 7  value=> 3
#index=> 8  value=> 2
#index=> 9  value=> 1
#index=> 10  value=> 0


#遍历字典时，可以用 iteritems() 函数同时得到键和键对应的值:
knights = dict([('gallahad','the pure'), ('robin','the brave')]);
for key,value in dict.iteritems(knights):
    print 'key=>',key,' value=>',value;
#for key,value in knights.iteritems():#同上
#    printo'key=>',key,' value=>',value;

#keyy=> gallahad  value=> the pure
#keyy=> robin  value=> the brave

