#-*- encoding: utf-8 -*-
from copy import deepcopy

data = {
    "name": "alex",
    "age": 18,
    "scores": {
        "语文": 130,
        "数学": 60,
        "英语": 98,
    }
}
d2 = data.copy()
d3 = deepcopy(data)

data["age"] = 20

data["scores"]["数学"] = 77
print(d3)
print(data)

# 赋值 :每一层都指向同一内存地址
# 浅copy：复制了壳子，第二层及以后的层都指向同一内存地址
# 深copy： 完全复制，对于可变类型的值，开辟新的内存地址，对于不可变的，指向同一内存地址。