#!/usr/bin/python
# coding=utf-8
# class


class MyClass:
    """a simple example class"""
    # 类变量，实例所共享的变量
    myFavoriteFruits = []

    # 构造函数
    def __init__(self, name):
        self.name = name  # 实例变量

    def addMyFavoriteFruits(self, fruit):
        self.myFavoriteFruits.append(fruit)

# define class end

# 实例化MyClass
instance1 = MyClass("zhaoyingnan")
instance2 = MyClass("mengdi")
print(instance1.name)  # zhaoyingnan
print(instance2.name)  # mengdi

# 可见类变量是实例所共享的
instance1.addMyFavoriteFruits("apple")
print(instance1.myFavoriteFruits)  # ['apple']
instance2.addMyFavoriteFruits("banana")
print(instance1.myFavoriteFruits)  # ['apple', 'banana']
