#-*- encoding: utf-8 -*-
## 迭代器
# city = ['beijing', 'shanghai', 'tinajin', 'chongqin']
# i = iter(city)
# print(type(i))
#
# print(i.__next__())  # 方式一：使用__next__()方法使用迭代器
# print(i.__next__())
# print('--------------')
# for i in i:  # 方式二：使用for循环使用迭代器
#     print(i)


# 迭代器：带状态的对象，在调用__next__()方法时返回容器中下一个值，任何内部实现了__iter__()和__next__()方法的对象，都是迭代器。
# __iter__()返回迭代器本身，__next__()返回容器中下一个值，如果容器中没有更多元素了，则抛出StopIteration异常，至于它们到底是如何实现的这并不重要。

## 生成器
# def gggenerator(low, high):
#     while low <= high:
#         yield low  # yield和return一样，将low返回出去，然后卡住不动，直到下一次使用next()方法将其唤醒
#         low += 1
#
#
# for i in gggenerator(1, 10):
#     print(i, end='')


# 定义：一个函数，内部如果包含yield关键字，那么这个函数就是个生成器
# 组成：生成器有两部分组成，生成器的函数、生成器的迭代器。生成器的函数是由def定义包含yield部分，生成器的迭代器是这个函数返回的部分（暗指gggenerator(1,10)）,
# 这个迭代器内部实现了__iter__()和__next__()方法

# 生成器产生无限多的值
# def generator(start=0):
#     while True:
#         yield start
#         start += 1
#
#
# for number in generator(4):
#     print(number, end='')
#     if number > 20:
#         break



















