# -*- encoding: utf-8 -*-
### 装饰器
## 基础写法

# def timer(func):
#     def inner(*args, **kwargs):
#         print('.....执行test前的操作.....')
#         ret = func()
#         print('.....执行test后的操作......')
#         return ret
#     return inner
#
# @timer
# def test():
#     print('......in test......')
# test()

## 给函数添加两个装饰器

# import time
# def how_much_time(func):
#     print('.........in how_much_time.........')
#     def inner():
#         t_start = time.time()
#         print('......1.....')
#         func()
#         t_end = time.time()
#         print('一共花费了%d秒时间' % (t_end - t_start))
#     return inner
#
# def mylog(func):
#     print('.........in mylog.........')
#     def inner():
#         print('......start.......')
#         func()
#         print('......end........')
#     return inner
#
# @how_much_time
# @mylog  # 执行顺序(凸形)：先执行mylog外部代码---->再执行how_much_time外部代码---->再执行how_much_time内部代码---->再执行mylog内部代码
# def sleep_5s():
#     time.sleep(5)
#     print("%d秒结束了！" % (5,))
#
# if __name__ == '__main__':
#     sleep_5s()

## 带参数的装饰器

# def mylog(type):
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             if type =='文件':
#                 print('.......文件中........')
#             else:
#                 print('.......非文件中............')
#             return func(*args, **kwargs)
#         return inner
#     return wrapper
#
# @mylog('文件') # 如果一个装饰器要加参数，那么就需要在这个装饰器外层嵌套一个函数，参数写在函数里
# def func2(a, b):
#     print('.......in func2.....',a, b)
#
# if __name__ == '__main__':
#     func2(100, 200)


## 带参数的类装饰器

import time


class Decorator:
    def __init__(self, func):
        self.func = func
    def defer_time(self, time_sec):
        time.sleep(time_sec)
        print('........延迟了%d秒，延迟结束了.......' % time_sec)
    def __call__(self, time): # 实际上 5 会被传到这里赋值给time
        self.defer_time(time)
        self.func()

@Decorator
def f1():
    print('......延迟之后我才执行.........')
f1(5)

