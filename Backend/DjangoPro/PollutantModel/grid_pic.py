from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.basemap import Basemap
import cmaps
import math

# lat_lon是个列表嵌套，列表中6000个小列表，每个小列表中7000个0
# [
#     [0.0.0.0.0.......7000个0],
#     [],
#     [],
#     ...
#     ...6000列
# ]
lat_lon = []
for i in range(6000):
    lat_lon.append([])
    for j in range(7000):
        lat_lon[i].append(0)
merge_path = '/Users/apple/Pypro/Backend/DjangoPro/PollutantModel/merged_result/'
# df1 = open(merge_path + '201901.csv', 'r', encoding='utf-8-sig')
# 测试结果文件
df1 = open(merge_path + 'test.csv', 'r', encoding='utf-8-sig')
List = []
# 将结果总文件里的每行都封装到一个小列表中，小列表组成一个总列表List
for line in df1.readlines():
    line = line.split(',')
    List.append(line)
print(List)
print(len(List))
# List: [['port','pollutant','lng','lat','value'],['上海', 'bc1', '113.98', '30.7', '0.003\n'],[],[]]




# 给矩阵lat_lon赋予value值
for i in range(0, len(List)):
    # lng*100, lat*100 取小数点后两位，利用math.floor取向下舍入的数字
    if i != 0:
        ilon = math.floor(round(float(List[i][2]) * 100, 2)) - 7000  # math.floor-返回一个整数 int，表示向下舍入的数字
        ilat = math.floor(round(float(List[i][3]) * 100, 2))
        value = str.strip(List[i][4])
        print(ilon, ilat, value)
        lat_lon[ilat][ilon] += float(value)
print('======finale======')
# print(lat_lon)





fig = plt.figure()
ax = fig.add_subplot(111) # “111”表示“1×1网格，第一子图”，“234”表示“2×3网格，第四子图”
# basemap = Basemap(llcrnrlon=119.7, llcrnrlat=29, urcrnrlon=122.7, urcrnrlat=32)

basemap = Basemap(llcrnrlon=118.92, llcrnrlat=31.5, urcrnrlon=120.01, urcrnrlat=32.4)
# llcrnrlon：longitude of lower left hand corner of the desired map domain (degrees).所需映射域左下角的经度(度)。
# llcrnrlat：latitude of lower left hand corner of the desired map domain (degrees).所需映射域左下角的纬度(度)。
# urcrnrlon：longitude of upper right hand corner of the desired map domain (degrees).所需映射域右上角的经度(度)。
# urcrnrlat： latitude of upper right hand corner of the desired map domain (degrees).所需映射域右上角的纬度(度)。

# worldMap = basemap.readshapefile(r'D:\pollution\city\city', 'city')
# data = [[lat_lon[i][j] for j in range(len(lat_lon[0]))] for i in range(len(lat_lon))]
# cm = cmaps.precip3_16lev
# im = plt.imshow(data, interpolation='None', extent=(70, 140, 60, 0), cmap=cm, norm=LogNorm(vmin=1, vmax=10000))
# divider = make_axes_locatable(ax)
# cax = divider.append_axes('right', size='5%', pad=0.05)
# plt.colorbar(im, cax=cax)
# plt.savefig(r'D:\pollution\pic\zj_nox.png', dpi=1000)
