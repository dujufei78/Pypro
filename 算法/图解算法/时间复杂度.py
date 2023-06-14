#-*- encoding: utf-8 -*-
# 时间复杂度：O(logN)
def algorithm(N):
    count = 0
    i = N
    while i > 1:
        i = i / 2
        count += 1
    return count

# 时间复杂度：O(NlogN)
# 两层循环相互独立，第一层和第二层时间复杂度分别为 O(logN) 和 O(N) ，则总体时间复杂度为O(NlogN) ；
def algorithm(N):
    count = 0
    i = N
    while i > 1:
        i = i / 2
        for j in range(N):
            count += 1


