# -*- encoding: utf-8 -*-


def func(st):
    l1 = ['(', '{', '[']
    l2 = [')', '}', ']']
    l3 = ['()', '{}', '[]']

    if len(st) % 2 != 0:
        return False
    res = []

    for i in st:
        print('....i is %s' % i)
        if i in l1:
            res.append(i)
        elif i in l2:
            if res.pop() + i not in l3:
                return False
    if not res:
        return True
    return False

if __name__ == '__main__':
    s = "()[[{}"
    res = func(s)
    print(res)

