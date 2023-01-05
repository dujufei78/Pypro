#-*- encoding: utf-8 -*-
# 1. 多线程 join
import threading
import time

# def thread_job():
#     print('t1 start')
#     for i in range(5):
#         print(i)
#         time.sleep(0.1)
#     print('t1 end')
# t = threading.Thread(target=thread_job, name='t1')
# t.start()
# t.join()  # 等待子线程t执行完毕，再执行后边代码
# print('all done...')

# 2. 多线程的Quene功能
import threading
from queue import Queue


def job(l, q):
    for i in range(len(l)):
        l[i] = l[i] ** 2
    q.put(l)  # 将计算结果放到q


def multiThreading():
    q = Queue()
    threads = []  # 装四个线程
    data = [[1, 2, 3], [4, 5, 6], [6, 6, 6], [8, 8, 8]]
    for i in range(4):  # 运行四个线程
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    results = []  # 将结果从q队列中取出，放到result并输出、
    for _ in range(4):
        results.append(q.get())
    print('The results is: {}'.format(results))


if __name__ == "__main__":
    multiThreading()

# 3. 多线程GIL锁

import threading
from queue import Queue
import copy
import time

# def job(l, q):
#     res = sum(l)
#     q.put(res)
#
# def multithreading(l):
#     q = Queue()
#     threads = []
#     for i in range(4):
#         t = threading.Thread(target=job, args=(copy.copy(l), q), name='T%i' % i)
#         t.start()
#         threads.append(t)
#     [t.join() for t in threads]
#     total = 0
#     for _ in range(4):
#         total += q.get()
#     print(total)
# def normal(l):
#     total = sum(l)
#     print(total)
#
# if __name__ == '__main__':
#     # 不用多线程方法
#     l = list(range(1000000))
#     s_t = time.time()
#     normal(l * 4)
#     print('normal: ', time.time() - s_t)
#
#     # 用多线程方法
#     s_t = time.time()
#     multithreading(l)
#     print('multithreading: ', time.time() - s_t)


# 4. lock锁

import threading
# 无锁

# def job1():
#     global A
#     for i in range(10):
#         A+=1
#         print('job1',A)
#
# def job2():
#     global A
#     for i in range(10):
#         A+=10
#         print('job2',A)
#
# if __name__== '__main__':
#     A=0
#     t1=threading.Thread(target=job1)
#     t2=threading.Thread(target=job2)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()

import threading
# 有锁

# def job1():
#     global A,lock
#     lock.acquire()4
#     for i in range(10):
#         A+=1
#         print('job1',A)
#     lock.release()
#
# def job2():
#     global A,lock
#     lock.acquire()
#     for i in range(10):
#         A+=10
#         print('job2',A)
#     lock.release()
#
# if __name__== '__main__':
#     lock=threading.Lock()
#     A=0
#     t1=threading.Thread(target=job1)
#     t2=threading.Thread(target=job2)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()