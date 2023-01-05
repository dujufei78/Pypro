#-*- encoding: utf-8 -*-
import queue

q = queue.Queue()
for i in range(5):
    q.put(6)

print(q.qsize())