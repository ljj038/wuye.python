#!/usr/bin/python
# coding=utf-8
import os
# 目录操作

# os.getcwd()
# os.remove(file)
# os.chdir(path)  # 更改工作目录


# 创建目录
if(not os.path.isdir("./a/b/c")):
    os.makedirs("./a/b/c")  # 创建多级目录


# 返回目录下的文件
print(os.listdir("./"))


# 判断
# isdir
print(os.path.isdir("/alidata"))
# os.path.exists(path)
# isfile
print(os.path.isfile("/home/zhaoyingnan/psw"))
# islink
print(os.path.isfile("/home/zhaoyingnan/zwadmin"))
# ismount(path)
# isabs(path)  # Return True if path is an absolute pathname


# 返回绝对路径
print(os.path.abspath("../list/test01.py"))  # /home/zhao/wuye/list/test01.py
# realpath(path)


# 返回文件名部分
print(os.path.basename("../list/test01.py"))  # test01.py
# 返回路径部分
print(os.path.dirname("../list/test01.py"))  # ../list


# 文件信息
# getatime(path)
# getmtime(path)
# getctime(path)
# getsize(path)
print(os.stat("test01.py"))


# 分离文件名
print(os.path.split("../list/test01.py"))  # ('./list', 'test01.py')
# 分离扩展名
print(os.path.splitext("../list/test01.py"))  # ('./list/test01', '.py')
