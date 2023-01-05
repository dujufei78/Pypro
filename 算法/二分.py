# -*- encoding: utf-8 -*-


def binary_search(l, aim):
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
