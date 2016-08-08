#!/usr/bin/python
#coding=utf-8
#文件读写
#open(filename,mode) 函数返回文件对象

#mode:
#   'r'，此选项使文件只读
#   'w'，此选项使文件只写(对于同名文件，该操作使原有文件被覆盖)
#   'a'，此选项以追加方式打开文件
#   'r+'，此选项以读写方式打开文件
#   如果没有指定，默认为 'r' 模式。

f = open('num.txt', 'r');
print f;#<open file 'num.txt', mode 'r' at 0x7fd47d7af540>

#读取整个文件，或指定字符串长度的内容
#print f.read();

#读取一行
print f.readline();
f.close();

#按行读取文件内容
f = open('num.txt');
for line in f:
    print line,;#紧跟','忽律换行
f.close();

#readlines() 方法用于读取所有行(直到结束符 EOF)并返回列表，若给定sizeint>0
#返回总和大约为sizeint字节的行, 实际读取值可能比sizhint较大, 因为需要填充缓冲区。
#如果碰到结束符 EOF 则返回空字符串。
f = open('num.txt', 'r');
print f.readlines();#['1\n', '2\n', '3\n', '4\n', '5\n', '6\n', '7\n', '8\n', '9\n', '10\n']
f.close();

#write() 方法用于向文件中写入指定字符串
fwrite = open('write.txt', 'w');
list1 = ['a', 'b', 'c', 'd', 'e', 'f'];
for i in list1:
    #需要自己手动加上换行
    i+="\n";
    fwrite.write(i);
fwrite.close();


#从一个文件读，写入另一个文件
fread = open('num.txt', 'r');
fwrite = open('write2.txt', 'w');
for line in fread:
    fwrite.write(line);
fread.close();
fwrite.close();

#writelines() 方法用于向文件中写入一序列的字符串
#需要为列表的每个元素添加换行
for key,value in enumerate(list1):
    list1[key] = value+"\n";
print list1;#['a\n', 'b\n', 'c\n', 'd\n', 'e\n', 'f\n']
fwrite = open('write3.txt', 'w');
fwrite.writelines(list1);
f.close();

