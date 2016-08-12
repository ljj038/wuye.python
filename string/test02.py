#!/usr/bin/python
# coding=utf-8
from string import maketrans

""" 字符串大小写转换 start """
# 把字符串的第一个字符大写
print("apple".capitalize())  # Apple
# 所有单词的首字母大写
print("this is string example....wow!!!".title())  # This Is String Example....Wow!!!
# 将字符串转换为全小写
print("APPLE".lower())  # apple
# 将字符串转换为全大写
print("apple".upper())  # APPLE
# 翻转字符串中的大小写
print("aPpLE".swapcase())  # ApPle
# 判断一个字符串是否都为小写
print("apple".islower())  # True
# 判断一个字符串是否都为大写
print("APPLE".isupper())  # True

""" 字符串大小写转换 end """


""" 字符串填充 start """
# 返回一个字符串在中间 两边用指定字符(默认为空格)将字符串填充到指定的长度
print("apple".center(11, "-"))  # ---apple---
# 返回一个原字符串左对齐,并使用指定字符(默认空格)填充至指定长度的新字符串 指定的长度小于原字符串的长度则返回原字符串
print("apple".ljust(50, "-"))  # apple---------------------------------------------
# 返回一个原字符串右对齐,并使用指定字符(默认空格)填充至指定长度的新字符串 指定的长度小于原字符串的长度则返回原字符串
print("apple".rjust(50, "-"))  # ---------------------------------------------apple
# 方法返回指定长度的字符串，原字符串右对齐，前面填充0
print("apple".zfill(50))  # 000000000000000000000000000000000000000000000apple
""" 字符串填充 end """


""" 字符串统计 start """
# 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
print("apple".count("p"))  # 2
""" 字符串统计 end """


""" 字符串搜索 start """
# 判断字符串是否以指定字符串结尾
print("test01.py".endswith(".py"))  # True
# 判断字符串是否以指定字符串开始
print("test01.py".startswith("te"))  # True
# 搜索指定字符串在字符串中的开始的索引位置 否则返回-1
# index()方法与find()一样 但是在为发现指定字符串时会报一个异常
# rfind() rindex()是从右边开始搜索
print("apple".find("p"))  # 1
print("apple".find("d"))  # -1
# 返回字符串中的最大值
print(max("apple"))  # p
print(min("apple"))  # a
# 返回字符串中的最小值
""" 字符串搜索 end """

""" 字符串替换 start """
# 把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8(可指定数量)
print("app\tle".expandtabs(1))
# 去掉字符串左边的指定字符(默认为空格)
print("  banana".lstrip())  # banana
# 去掉字符串右边的指定字符(默认为空格)
print("banana  ".rstrip())  # banana
# 去掉字符串两边的指定字符(默认为空格)
print(" banana ".strip())  # banana
# 批量替换
trantab = maketrans("abef", "1234")  # 必须引入(from string import maketrans)
print("abcdef".translate(trantab))  # 12cd34  创建替换的映射关系后替换

""" 字符串替换 end """


""" 字符串编码 start """
# 以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors
# 指定的是'ignore'或者'replace'
print("apple".encode("base64", "strict"))  # YXBwbGU=

# 以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除 非 errors 指 定 的 是
# 'ignore' 或 者'replace'
print("YXBwbGU=".decode("base64", "strict"))  # apple
""" 字符串编码 end """


""" 字符串判断 start """
# 如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
print("12345".isalnum())  # True
print("12345aaa".isalnum())  # True
print("b12345aaa".isalnum())  # True
# 如果 string 至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
print("123".isalpha())  # False
print("123a".isalpha())  # False
print("abd".isalpha())  # True
# 如果 string 只包含数字则返回 True 否则返回 False
print("12345".isdigit())  # True
# 判读一个字符串是否只包含空格
print("".isspace())  # False
print(" ".isspace())  # True
""" 字符串判断 end """

""" 字符串拼接 start """
list1 = ["a", "b", "c"]  # 必须为字符串序列
tuple1 = ("a", "b", "c")
print("-".join(list1))  # a-b-c
print("-".join(tuple1))  # a-b-c
""" 字符串拼接 start """


""" 字符串分割 start """
str = "Line1-abcdef Line2-abc Line4-abcd"
# 使用 split 分割(默认分隔符为空格) 可以指定分割次数 返回列表(不包含分隔符)
print(str.split())  # ['Line1-abcdef', 'Line2-abc', 'Line4-abcd']
print(str.split(" ", 1))  # ['Line1-abcdef', 'Line2-abc Line4-abcd']
# 使用 partition 分割(默认分隔符为空格) 返回元组(只分割一次并且包含分隔符)
# rpartition() 从右边开始分割
print(str.partition(" "))  # ('Line1-abcdef', ' ', 'Line2-abc Line4-abcd')
""" 字符串分割 end """
