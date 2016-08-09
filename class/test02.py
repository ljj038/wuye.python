#!/usr/bin/python
# coding=utf-8
# 继承


class Animal:
    """继承"""

    def __init__(self):
        pass

    def eat(self):
        print("basic class")


class Dog(Animal):
    """Dog类继承Animal类"""

    # @override
    def eat(self):
        return "my favorite food is bone"

dog = Dog()
print(dog.eat())  # None 此时未override
print(dog.eat())  # my favorite food is bone

# isinstance()用于检查实例的类型
print(isinstance(dog, Dog))  # dog为实例 Animal为类名
print(isinstance(dog, Animal))
print(isinstance(1, int))

# issubclass() 用于检查类继承
print(issubclass(Dog, Animal))  # 必须是两个类名
print(issubclass(bool, int))
