项目总体流程
1.利用pycharm搭建python3的虚拟环境pollutvenv、创建项目PollutantModel；

2.虚拟环境中安装matplotlib、mpl_toolkits、Basemap、cmaps、numpy、pandas等第三方模块（第三方包的详细版本见项目根目录下requirements.txt文件）；
注：安装basemap-1.2.1-cp36-cp36m-win_amd64.whl（https://www.lfd.uci.edu/~gohlke/pythonlibs/#basemap）

3.功能逻辑一
【需求描述】：首先，统计2019年1月数据的排放数据【结果】（result_201901_new里的结果文件，这是钱老师在服务器上跑的【结果】文件，是用2019年1月份20%的车辆数据得到的结果）；
        接着，将统计得到的【结果】里的污染物排放总量，与天琦学姐论文里的数据做一个比对。

【功能实现】：将result文件中的n_grid.csv文件（各种污染物的排放数据），把这些文件里的数据按照污染物种类归并到一起,整理成类似sh_nox.csv文件一样；

合并方法：
import os
import pandas as pd
# 输入待合并文件所在文件夹
path = r'D:/work/BP/5/!
file list = []for file in os .listdir(path):# print(file)df = pd.read csv(path + file)file list.append(df)
result = pd.concat(file list) # 合产文件index=False) # 保存合并后的文件result.to csv(path +hard 5.csv'，

4.功能逻辑二
【需求描述】：绘制排放空间分布图（看看关于各污染物排放量的计算是否合理，如果没问题的话可以让钱老师接着在服务器上运行下去）。

【功能实现】：将功能逻辑一中整理得到的结果文件传入grid_pic.py中，执行绘制排放空间分布图。

备注：
安装basemap\basemap-data-hires:https://mirrors.bfsu.edu.cn/anaconda/pkgs/main/osx-arm64/
安装pyproj:https://www.lfd.uci.edu/~gohlke/pythonlibs/