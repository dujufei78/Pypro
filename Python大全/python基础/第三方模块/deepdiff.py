# distutils: language=3
# cython: language_level=3
# -*- coding: utf-8 -*-
# @Time    : 2024/2/4 16:47
# @Author  : dujufei-jk
# @Description: 用于比较两个json的不同之处

import json
from deepdiff import DeepDiff

# 读取两个JSON文件
with open('x86-85.json', encoding='utf-8') as f1, open('pyz_res.json', encoding='utf-8') as f2:
    json_data1 = json.load(f1)
    json_data2 = json.load(f2)

    # 使用DeepDiff比较差异
    diff = DeepDiff(json_data1, json_data2)

    # 打印差异信息
    print(diff)
