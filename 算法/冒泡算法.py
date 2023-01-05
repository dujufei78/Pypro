# -*- encoding: utf-8 -*-
import random


def bubble_sort(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


l = list(range(0, 20, 2))
random.shuffle(l)
print(l)
bubble_sort(l)
print(l)
