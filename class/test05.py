#!/usr/bin/python
# coding=utf-8
# 生成器 Generator
# Generator 是创建迭代器的简单而强大的工具
# 写起来就像是正规的函数，需要返回数据的时候使用 yield 语句
# generator保存的是算法，每次调用next()，就计算出下一个元素的值
# 直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误

# example:


def reverse(data):
    # range(start, stop[, step])
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse("apple"):
    print(char)

# 斐波拉契数列


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

for i in fib(10):
    print(i)


# 生成器表达式
# 和列表推导式很像:
# 列表推导式
print([i*i for i in range(1, 11) if i % 2 == 0])  # [4, 16, 36, 64, 100]
# 生成器表达式
a = (i*i for i in range(1, 11) if i % 2 == 0)
# <generator object <genexpr> at 0x7fad5f5b8938>
for i in a:
    print(i)
