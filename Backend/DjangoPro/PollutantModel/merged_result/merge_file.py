# -*- encoding: utf-8 -*-
import os
import pandas as pd

# 待合并文件所在文件夹
path = '/Users/apple/Pypro/Backend/DjangoPro/PollutantModel/data/reqult_201901_new/'

file_list = []
row_num = 0 # 统计符合条件的文件总行数
for file in os.listdir(path):
    path_final = path + file
    if path_final.endswith('_grid.csv'):
        print(path_final)
        df = pd.read_csv(path + file)
        print(len(df))
        row_num += len(df)
        file_list.append(df)
print(len(file_list))
print(row_num)
result = pd.concat(file_list) # 合并文件
merge_path = '/Users/apple/Pypro/Backend/DjangoPro/PollutantModel/merged_result/'
# 写入合并后的文件
# result.to_csv(merge_path +'201901.csv',index=False)
