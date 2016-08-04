#!/usr/bin/python
#coding=utf-8
#包内引用

#调用 my_string.filters.replace._replace()
#from my_string.filters import replace;#可以这样写
from ..filters import replace;#也可以这样写
replace._replace();

if(__name__ == '__main__'):
    pass;
else:
    print "import my_string.formats.dump moudle";
