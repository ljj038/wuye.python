#!/usr/bin/python
#coding=utf-8
#字符串/转义/多行/拼接/重复/索引/切片
print 'hello wuye';#单引号
print 'doesn\'t';#用\转义单引号
print "doesn't";#用双引号
print '"yes",he said.';#单引号嵌套双引号
print "\"yes\",he said.";#双引号嵌套双引号
#如果前面带有\的字符被当作特殊字符，可以用\转义，也可以在前面加r
print 'C:\\some\\name';
print r'C:\some\name';

#字符串文本能够分成多行:
##方法是使用三引号："""...""" 或者 '''...'''。行尾换行符会被自动包含到字符串中，但是可以在行尾加上 \ 来避免这个行为
print """
        Usage: thingy [OPTIONS]
        -h                        Display this usage message
        -H hostname               Hostname to connect to
"""

print """\
        Usage: thingy [OPTIONS]
        -h                        Display this usage message
        -H hostname               Hostname to connect to\
"""

#字符串拼接
print 'my ' + 'name';
#相邻的两个字符串文本会自动拼接在一起,但是只能用于两个字符串文本，不能用于字符串表达式
#如果你想连接多个变量或者连接一个变量和一个字符串文本，使用 +
print 'my ' 'name';
prefix = 'Py';
#print prefix 'thon';#can't concatenate a variable and a string literal
print prefix + 'thon';

#字符串重复
print 'a' + 2*'p' + 'le';

#字符串也可以被检索，第一个索引为0
word = 'python';
print word[0];
#索引也可以是负数，这将会从右边开始计算，最右边的索引为-1
print word[-1];

#字符串还支持切片，索引用于获取单个字符串，切片可以获得一个子字符串
#+---+---+---+---+---+---+
#| P | y | t | h | o | n |
#+---+---+---+---+---+---+
#0   1   2   3   4   5   6
#-6  -5  -4  -3  -2  -1
print word[0:2];#"py"  characters from position 0 (included) to 2 (excluded)
print word[2:5];#"tho" characters from position 2 (included) to 5 (excluded)
print word[:2];#py
print word[2:];#thon

print word[:2] + word[2:];#python 这种方法永远等于这个字符串

#获取字符串长度
print len(word);
