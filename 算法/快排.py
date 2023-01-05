# -*- encoding: utf-8 -*-
import random


def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left


def quick_sout(li, left, right):
    if left < right:
        mid= partition(li , left, right)
        quick_sout(li, left, mid - 1)
        quick_sout(li, mid + 1, right)

li = list(range(0, 20, 3))
print(li)
random.shuffle(li)
print(li)
quick_sout(li, 0, len(li) - 1)
print(li)