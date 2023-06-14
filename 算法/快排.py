# -*- encoding: utf-8 -*-
import random


def partition(li, left, right):
    '''
    归位函数
    li = [5,1,4,2,3,7,8,9,6,0]
    '''
    tmp = li[left]  # 先把5取出来
    while left < right:
        while left < right and li[right] >= tmp:  # 当满足右边元素大于5时，指针左移，直到找到比归位元素5小的数
            right -= 1  # 从5的右边找比5小的
        li[left] = li[right]  # 将找到的比5小的值，赋值给5的元素坑里
        while left < right and li[left] <= tmp:  # 当满足左侧元素小于5时，指针右移，直到找到比归位元素5大的值
            left += 1  # 从5左右找比5大的
        li[right] = li[left]
    li[left] = tmp  # 如果跳出循环，说明5左侧都小于5，5右侧都大于5，左右指针重合，将5放到这个指针重合的位置
    return left


def quick_sout(li, left, right):
    '''
    思路：采用递归思想，对所选元素进行归位
    实现：首先选取出最左边元素p作为归位元素，p的坑为左指针，列表最右侧元素为右指针，
    将右指针依次左移，直至找到比p小的元素x，放到p的坑里，然后左指针右移，直到找到比p元素大的元素，
    放到x的坑里，一直执行，直至左右指针重合，将p放到指针重合的坑里，p归位完成。现在，p左侧都是比p小的元素，右边都比p大。
    继续，使用递归思想，对p左侧区域和右侧区域进行排序。即可
    时间复杂度：O(nlogn)
    '''
    if left < right:
        mid = partition(li, left, right)
        quick_sout(li, left, mid - 1)  # 递归，同理，对归位元素5左侧进行排序
        quick_sout(li, mid + 1, right)  # 递归，同理，对5右侧进行排序


li = list(range(0, 20, 3))
print(li)
random.shuffle(li)
print(li)
quick_sout(li, 0, len(li) - 1)
print(li)
