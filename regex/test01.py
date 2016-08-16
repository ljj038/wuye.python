#!/usr/bin/python
# coding=utf-8
# 正则
import re
email = '791520450@qq.com'
# 创建一个 pattern 对象
pattern = re.compile(r'\d+')
# print(pattern)  # <_sre.SRE_Pattern object at 0x7fe0f66efdd8>

# 将结果(match对象)赋值给变量 None表示没有匹配到结果
# pattern 对象中有分组()则会返回元组 否则返回字符串
ma = re.match(pattern, email)
# print(ma)  # <_sreSRE_Match object at 0x7fee7ff49850>

# 获取匹配结果在原字符串中的索引位置
print(ma.span())  # (0, 9)

# 获取被操作的字符串
print(ma.string)  # 791520450@qqcom

# search 使用方法
pattern = re.compile(r'dog', re.I)
match = pattern.search('adogs', 1, 4)
print(match.group(0))  # dog
print(match.start())  # 1 返回开始位置的索引值
print(match.end())  # 4 返回结束位置的索引值
print(match.span())  # (1, 4) 返回开始和结束位置的索引值的元组

# groupdict 使用方法
match = re.match(r'(?P<firstName>\w+) (?P<lastName>\w+)', 'zhaoyingnan zhaoyn')
print(match.groupdict())  # {'lastName': 'zhaoyn', 'firstName': 'zhaoyingnan'}

# groups() gruop() lastgroup()
# 当使用分组时 match 为一个元组 此时用 groups() 获取该元组 用group() 获取单个或多个指定的元组
# 当未使用分组时 match 为一个字符串 可以使用 group() 直接获取该匹配
pattern = re.compile(r'(\d)(\d)(\d)(?P<lastGroupName>\d)')
match = pattern.match('1982')
print(match.groups())
print(match.group(1, 3))  # 若结果为元组时 元组的第一个元素为被操作的字符串
print(match.lastgroup)  # 获取最后一个组的组名


# split() 分割 返回列表
print(re.split(r'\W', 'melon apple'))  # ['melon', 'apple']
str1 = 'python:java C++,php'
print(re.split(r':| |,', str1))  # ['python', 'java', 'C++', 'php']

# findall() 贪婪 返回列表
print(re.findall(r'\w', 'melon'))  # ['m', 'e', 'l', 'o', 'n']


def add(match):
    val = int(match.group())
    return str(val*2)

# sub(pattern, replace or function, str, count=0, flags=0) 字符串替换 返回替换后的字符串
str1 = 'Baked Beans And Spam'
print(re.sub(r'\sand\s', ' & ', str1, flags=re.I))  # Baked Beans & Spam

print(re.sub(r'\d+', add, '1 2 3'))  # 2 4 6
exit()


# search() findall()
str1 = '110 120 130 140'
pattern = re.compile(r'\d+')
# return a match object
match = pattern.search(str1)
print(match.group())  # 110
# return a list
match = pattern.findall(str1)
print(match)  # ['110', '120', '130', '140']
print(sum([int(x) for x in match]))  # 500


# 综合
str1 = '791520450@163.com ximing@qq.com zhaoyn@bbtree.cn'
print(re.findall(r'[\w\d_]{3}[\w\d_]*@[\w\d_]+.(?:com|cn)', str1))
