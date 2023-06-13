# -*- encoding: utf-8 -*-


def binary_search(l, aim):
    '''
    传参：一个有序列表，和目标值，寻找某一个元素的索引
    解决方法：首先，生成大小两个指针，在不是空列表的情况下，拿着最中间的元素进行遍历比对，，
        如果目标值比中间值大，那么小指针右移到中间值位置右边一位；
        如果目标值比中间值小，那么大指针左移到中间值位置左边一位；
        依次进行。
    时间复杂度：O（logn）
    '''
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if aim < l[mid]:
            high = mid - 1
        elif aim > l[mid]:
            low = mid + 1
        else:
            return mid
    else:
        return -1


aim = 4
l = list(range(0, 30))
res = binary_search(l, aim)
print(res)
