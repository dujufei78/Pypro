#-*- encoding: utf-8 -*-
# 列表删除,删除最后一个元素
L = [1, 2, 3, 4]
L.pop()
print(L)

# 列表扩展
fruit1 = ['apple', 'orange']
fruit2 = ['pear', 'grape']
fruit1.extend(fruit2)
print(fruit1)

# 字典删除
fruit = {1: 'apple', 2: 'orange', 3: 'grape', 'third': '111'}
fruit.pop('third')
print(fruit)

# 集合创建
fruit = set(['apple', 'orange', 'pear'])
fruit.add('banana')  # add添加一个，update添加多个
print(fruit)
fruit.update('a', 'b')
print(fruit)

# 集合删除
fruit.pop()  # 随机删除
print(fruit)
fruit.remove('a')
print(fruit)