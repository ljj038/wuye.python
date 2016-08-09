#!/usr/bin/python
# coding=utf-8
# 迭代器
# 大多数容器对象都能被for遍历:
for element in [1, 2, 3]:
    print(element)

for element in (1, 2, 3):
    print(element)

for key in {'one': 1, 'two': 2}:
    print(key)

for char in 'abc':
    print(char)

for line in open('../file/num.txt', 'r'):
    print(line)

# for 语句在容器对象中调用 iter()
# iter() 函数返回一个定义了 next() 方法的迭代器对象，它在容器中逐一访问元素
# 没有后续的元素时，next() 抛出一个 StopIteration 异常通知 for 语句循环结束
# 以下是其工作原理的示例:
# s = "abs"
# it = iter(s)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# Traceback (most recent call last):
#     File "<stdin>", line 1, in ?
#     next(it)
#     StopIteration

# 为自己的类添加迭代器行为


class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, your_str):
        self.data = your_str
        self.index = len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        if(self.index == 0):
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

reverse = Reverse("hello")
for char in reverse:
    print(char)
