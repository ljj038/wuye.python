#!/usr/bin/python
#coding=utf-8

#for
words = ['linux', 'windows'];
for s in words:
    print s, len(s);

#通过索引来迭代
for index in range(len(words)):
    print index, words[index], len(words[index]);


#while
#continue,
i = 0;
while i < 10:
    i += 1;
    if i%2 == 0:
        continue;
    print i;

#break
j = 0;
while 1:
    j += 2;
    if j > 10:
        break;
print j;
