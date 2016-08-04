#!/usr/bin/python
#coding=utf-8
#输出
#格式化输出:
#str.format()
price = {'apple':3, 'banana':5, 'pear':10};
for index,value in dict.iteritems(price):
    print "水果{name:10}=> 单价{price:.2f}{fix}".format(name=index, price=value, fix='￥');
#水果pear      => 单价10.00￥
#水果apple     => 单价3.00￥
#水果banana    => 单价5.00￥

#传入一个字典，用中括号( '[]' )访问它的键
print "水果apple=> 单价{[apple]:.2f}{fix}".format(price, fix='￥');#水果apple=> 单价3.00￥


#%操作符
for index,value in price.iteritems():
    print "水果%s=> 单价%.2f%s"%(index, value, '￥');
#水果pear=> 单价10.00￥
#水果apple=> 单价3.00￥
#水果banana=> 单价5.00￥

