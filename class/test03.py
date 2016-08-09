#!/usr/bin/python
# coding=utf-8
# 私有变量

# 只能从对像内部访问的“私有”实例变量，在 Python 中不存在
# 然而，也有一个变通的访问用于大多数 Python 代码:
# 以一个下划线开头的命名(例如  _spam )会被处理为API的非公开部分
# (无论它是一个函数、方法或数据成员)
# 它会被视为一个实现细节，无需公开。

# 因为有一个正当的类私有成员用途(即避免子类里定义的命名与之冲突)
# Python 提供了对这种结构的有限支持，称为 name mangling (命名编码)
# 任何形如 __spam 的标识(前面至少两个下划线，后面至多一个)
# 被替代为 _classname__spam ，去掉前导下划线的 classname 即当前的类名
# 此语法不关注标识的位置，只要求在类定义内

# 名称重整是有助于子类重写方法，而不会打破组内的方法调用,如:


class Mapping:
    def __init_(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update  # private copy of original update() method


class manglingSubClass(Mapping):

    def update(self, key_list, value_list):
        for item in zip(key_list, value_list):
            self.items_list.append(item)
