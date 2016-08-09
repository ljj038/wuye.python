#!/usr/bin/python
# coding=utf-8
# os 操作系统相关
import os

# os.error 内建OSError exception的别名

# os.name 导入依赖操作系统模块的名字
# 可能返回 'posix', 'nt', 'os2', 'ce', 'java', 'riscos'
print(os.name)

print(os.environ)  # 函数提供的信息或操作和当前的用户以及进程相关

# 返回代表当前工作目录的字符串
print(os.getcwd())  # /home/zhaoyingnan/wuyepython/standard_library

# os.chdir('/server/accesslogs')  # Change current working directory
# os.system('mkdir today')   # Run the command mkdir in the system shell
