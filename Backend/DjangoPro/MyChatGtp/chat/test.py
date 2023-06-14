# -*- encoding: utf-8 -*-
# from threading import Thread
#
# from matplotlib.colors import LogNorm
# import matplotlib.pyplot as plt
# from mpl_toolkits.axes_grid1 import make_axes_locatable
# from mpl_toolkits.basemap import Basemap
# import cmaps
# import math
#
# from multiprocessing import Process
#
#
#
# def Drawing_map(pollution, map):
#     print(pollution, map)
#     '''
#     第一步：构造lat_lon，lat_lon是个列表嵌套，列表中6000个小列表，每个小列表中7000个0
#     '''
#     # [
#     #     [0.0.0.0.0.......7000个0],
#     #     [],
#     #     [],
#     #     ...
#     #     ...6000列
#     # ]
#
#     lat_lon = []
#     for i in range(6000):
#         lat_lon.append([])
#         for j in range(7000):
#             lat_lon[i].append(0)
#     # merge_path = 'merged_result/test.csv'
#     merge_path = 'merged_result/201901data/201901{}.csv'.format(pollution)
#     # df1 = open(merge_path + '201901.csv', 'r', encoding='utf-8-sig')
#
#     # 测试结果文件
#     # df1 = open(merge_path + 'test.csv', 'r', encoding='utf-8-sig')
#
#     df1 = open(merge_path, 'r', encoding='utf-8-sig')
#     List = []
#     # 将结果总文件里的每行都封装到一个小列表中，小列表组成一个总列表List
#     for line in df1.readlines():
#         line = line.split(',')
#         List.append(line)
#     # List: [['port','pollutant','lng','lat','value'],['上海', 'bc1', '113.98', '30.7', '0.003\n'],[],[]]
#     print('=====1=====')
#
#     try:
#         '''
#         第二步：给矩阵lat_lon赋予value值
#         '''
#         for i in range(0, len(List)):
#             # lng*100, lat*100 取小数点后两位，利用math.floor取向下舍入的数字
#             if i != 0:
#                 ilon = math.floor(round(float(List[i][2]) * 100, 2)) - 7000  # math.floor-返回一个整数 int，表示向下舍入的数字
#                 ilat = math.floor(round(float(List[i][3]) * 100, 2))
#                 value = str.strip(List[i][4])
#                 # print(ilon, ilat, value)
#                 lat_lon[ilat][ilon] += float(value)
#     except Exception as e:
#         print(str(e))
#     print('====3=====')
#
#     try:
#         '''
#         第三步：画各种污染物空间信息发布图
#         '''
#         fig = plt.figure()
#         ax = fig.add_subplot(111)  # “111”表示“1×1网格，第一子图”，“234”表示“2×3网格，第四子图”
#         # basemap = Basemap(llcrnrlon=119.7, llcrnrlat=29, urcrnrlon=122.7, urcrnrlat=32)
#         # 镇江港经纬度
#         # basemap = Basemap(llcrnrlon=118.92, llcrnrlat=31.5, urcrnrlon=120.01, urcrnrlat=32.4)
#         # china经纬度
#         # basemap = Basemap(llcrnrlon=74, llcrnrlat=4, urcrnrlon=136, urcrnrlat=54)
#
#         # 珠江三角洲经纬度
#         basemap = Basemap(llcrnrlon=115.7, llcrnrlat=28, urcrnrlon=123, urcrnrlat=34.5)
#
#         # llcrnrlon：longitude of lower left hand corner of the desired map domain (degrees).所需映射域左下角的经度(度)。
#         # llcrnrlat：latitude of lower left hand corner of the desired map domain (degrees).所需映射域左下角的纬度(度)。
#         # urcrnrlon：longitude of upper right hand corner of the desired map domain (degrees).所需映射域右上角的经度(度)。
#         # urcrnrlat： latitude of upper right hand corner of the desired map domain (degrees).所需映射域右上角的纬度(度)。
#
#         # worldMap = basemap.readshapefile(r'D:\pollution\city\city', 'city')
#         worldMap = basemap.readshapefile(r'data\map\%s' % map, '%s' % map)
#
#         data = [[lat_lon[i][j] for j in range(len(lat_lon[0]))] for i in range(len(lat_lon))]
#         cm = cmaps.precip3_16lev
#         im = plt.imshow(data, interpolation='None', extent=(70, 140, 60, 0), cmap=cm, norm=LogNorm(vmin=1, vmax=10000))
#         divider = make_axes_locatable(ax)
#         cax = divider.append_axes('right', size='5%', pad=0.05)
#         plt.colorbar(im, cax=cax)
#         plt.savefig(r'distribution_map\test\zsj_%s.png' % pollution, dpi=1000)
#     except Exception as e:
#         print(str(e))
#     print('.......子进程执行中......')
#
#
# if __name__ == '__main__':
#     '''
#     传入两个参数：污染物种类、城市地图种类
#     '''
#     tasks_list = []
#     pollutant_class = ['nox', 'co', 'co2', 'pm']
#     map_class = ['YRD', 'all_region_new_polygon', 'Export_Output_2', 'shape_service_area_YRD_combine',
#                  'shape_service_area_YRD_raw', '长三角_市界', '高速_YRD']
#     for i in range(4):
#         p = Thread(target=Drawing_map, args=(pollutant_class[i], map_class[0],))  # map_class暂时写死,YRD
#         p.start()
#         tasks_list.append(p)
#
#     for p in tasks_list:
#         p.join()  # 当所有子进程执行完成，才会执行主进程
#
#     print('....主进程执行成功.....')
#
