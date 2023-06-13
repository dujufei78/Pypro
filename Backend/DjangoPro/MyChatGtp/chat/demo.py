#-*- encoding: utf-8 -*-
import time
from threading import Thread


def timer(func):
    def inner(*args, **kwargs):
        s_time = time.time()
        ret = func(*args, **kwargs)
        e_time = time.time()
        print('....执行主函数话费时间为：%s' % (e_time-s_time))
        return ret
    return inner


@timer
def Drawing_map(a,b):
    time.sleep(4)
    print(a,b)

if __name__ =='__main__':
    tasks_list = []
    pollutant_class = ['nox', 'co', 'co2', 'pm']
    map_class = ['YRD', 'all_region_new_polygon', 'Export_Output_2', 'shape_service_area_YRD_combine',
                 'shape_service_area_YRD_raw', '长三角_市界', '高速_YRD']
    for i in range(4):
        p = Thread(target=Drawing_map, args=(pollutant_class[i], map_class[0],))  # map_class暂时写死,YRD
        p.start()
        tasks_list.append(p)

    for p in tasks_list:
        p.join()

    print('.....主线程结束....')
