import pandas as pd
import csv
import numpy as np
from sklearn.cluster import DBSCAN
import shapefile
import shapely.geometry as shpgeo
import shapely.geometry as geometry
import time
import sys
import math
import gc



def retrieve_trace(data_file, limit=999999):  # 从文件中导入，需要对照数据库的方法进行修改
    trace_lngs = []
    trace_lats = []
    trace_speeds = []
    trace_ts = []
    prev_lng = 0.0
    prev_lat = 0.0
    prev_ts = -1
    prev_speed = -1
    count_raw = 0
    count_new = 0
    with open(data_file, encoding='UTF-8-sig') as fh:
        for line in fh:
            if count_raw > limit:
                break
            lineArray = line.replace('\n', '').split(',')
            id = int(lineArray[0])
            cur_lng = float(lineArray[1])
            cur_lat = float(lineArray[2])
            cur_ts = int(lineArray[3])
            cur_speed = int(lineArray[4])
            # 处理速度为0时的位置漂移，替换为前一个坐标点
            if cur_speed == 0 and prev_speed == 0:
                cur_lng = prev_lng
                cur_lat = prev_lat
                cur_speed = prev_speed
            # 处理速度为0时的缺失点，插入前一个坐标点
            while (cur_ts - prev_ts) > 40 and prev_ts >= 0:
                if prev_ts + 70 > cur_ts:  # 这一步为了让添加的最后一个record的timestamp正确而其他的保持差值为零，获得速度为零的持续时间，方便计算排放时将静止的筛去
                    trace_lngs.append(prev_lng)
                    trace_lats.append(prev_lat)
                    trace_speeds.append(prev_speed)
                    trace_ts.append(prev_ts + 30)
                    prev_ts += 30
                    count_new += 1
                else:
                    trace_lngs.append(prev_lng)
                    trace_lats.append(prev_lat)
                    trace_speeds.append(prev_speed)
                    trace_ts.append(trace_ts[count_new - 1])
                    prev_ts += 30
                    count_new += 1
            trace_lngs.append(cur_lng)
            trace_lats.append(cur_lat)
            trace_speeds.append(cur_speed)
            trace_ts.append(cur_ts)
            prev_lng = cur_lng
            prev_lat = cur_lat
            prev_ts = cur_ts
            prev_speed = cur_speed
            count_raw += 1
            count_new += 1
    print(count_raw, count_new)
    return trace_lngs, trace_lats, trace_speeds, trace_ts, id


def retrieve_trace_db(filename, car_sid):  # 从数据库导入，前处理函数
    trace_lngs_raw = []
    trace_lats_raw = []
    trace_speeds_raw = []
    trace_ts_raw = []
    trace_lngs = []
    trace_lats = []
    trace_speeds = []
    trace_ts = []
    trace_weights = []
    info = {}
    prev_lng = 0.0
    prev_lat = 0.0
    prev_ts = -1
    prev_speed = -1
    count_raw = 0
    count_new = 0
    threshold = 60
    results = []
    # 从数据库导入轨迹数据，对轨迹数据进行前处理
    #table_name = 'car_group_%d' % int(math.floor(car_sid / 10000.0))
    #dataSql = "SELECT lng,lat,timestamp,speed FROM %s WHERE car_sid = %d" % (table_name, car_sid)

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if int(row['car_sid']) == car_sid:
                results.append([float(row['lng']),float(row['lat']),int(row['timestamp']),int(row['speed'])])


    if len(results) > 120:  # 排除记录数过少的异常数据
        # 第一步，处理被折叠的轨迹，形成完整序列
        for item in results:
            cur_lng = float(item[0])
            cur_lat = float(item[1])
            cur_ts = int(item[2])
            cur_speed = int(item[3])
            while (cur_ts - prev_ts) > 40 and prev_ts >= 0 and prev_speed == 0:
                trace_lngs_raw.append(prev_lng)
                trace_lats_raw.append(prev_lat)
                trace_speeds_raw.append(prev_speed)
                trace_ts_raw.append(prev_ts + 30)
                prev_ts += 30
            trace_lngs_raw.append(cur_lng)
            trace_lats_raw.append(cur_lat)
            trace_speeds_raw.append(cur_speed)
            trace_ts_raw.append(cur_ts)
            prev_lng = cur_lng
            prev_lat = cur_lat
            prev_ts = cur_ts
            prev_speed = cur_speed
            count_raw += 1

        # 第二步，将连续速度为0的序列进行调整和压缩
        prev_speed = -1
        next_speed = -1
        zero_count = 0
        weight_count = 1
        for i in range(0, len(trace_lngs_raw)):
            cur_lng = trace_lngs_raw[i]
            cur_lat = trace_lats_raw[i]
            cur_ts = trace_ts_raw[i]
            cur_speed = trace_speeds_raw[i]
            if i < (len(trace_lngs_raw) - 1):
                next_speed = trace_speeds_raw[i + 1]
            else:
                next_speed = -1

            # 0速度序列的中间点的timestamp全部设置为前一个点的timestamp，计算连续为0的数量
            if cur_speed == 0 and prev_speed == 0:
                if next_speed == 0:
                    cur_ts = prev_ts
                zero_count += 1

            if zero_count < threshold:
                trace_lngs.append(cur_lng)
                trace_lats.append(cur_lat)
                trace_speeds.append(cur_speed)
                trace_ts.append(cur_ts)
                trace_weights.append(weight_count)
                count_new += 1
            else:
                if cur_speed == 0 and i == (len(trace_lngs_raw) - 1):  # 添加最后一个0速度点
                    trace_lngs.append(cur_lng)
                    trace_lats.append(cur_lat)
                    trace_speeds.append(cur_speed)
                    trace_ts.append(cur_ts)
                    trace_weights.append(weight_count)
                    count_new += 1
                weight_count += 1

            if cur_speed > 0 and prev_speed == 0:
                # 先处理之前的点，若zero_count没有超过，则不用管，如果zero_count超过，则前一个最后0速度点要添加
                if zero_count >= threshold:
                    trace_lngs.append(prev_lng)
                    trace_lats.append(prev_lat)
                    trace_speeds.append(prev_speed)
                    trace_ts.append(prev_ts)  # 速度转换点，添加本身的时间戳
                    trace_weights.append(weight_count - 1)
                    # 添加本身轨迹点
                    trace_lngs.append(cur_lng)
                    trace_lats.append(cur_lat)
                    trace_speeds.append(cur_speed)
                    trace_ts.append(cur_ts)
                    trace_weights.append(1)
                    count_new += 2
                zero_count = 0
                weight_count = 1

            prev_lng = cur_lng
            prev_lat = cur_lat
            prev_ts = cur_ts
            prev_speed = cur_speed
        info['count_raw'] = count_raw
        info['count_new'] = count_new
    else:
        print('Only %d data, not enough, exit!' % len(results))
        # exit()
        info['error'] = 'not enough data'
        return [], [], [], [], [], info

    # 粗筛轨迹是否经过长三角，不经过直接pass
    ts1 = int(time.time())
    count_port = 0
    traces_df = pd.DataFrame({'lng': trace_lngs, 'lat': trace_lats})
    port_area = [
        [118.34, 118.39, 31.35, 31.41],
        [118.58, 118.63, 31.93, 31.95],
        [119.04, 119.08, 32.18, 32.22],
        [119.36, 119.39, 32.19, 32.22],
        [119.62, 119.67, 32.17, 32.20],
        [120.40, 120.55, 31.95, 32.00],
        [120.76, 120.80, 31.34, 31.36],
        [120.93, 121.02, 31.74, 31.77],
        [121.19, 121.26, 31.60, 31.66],
        [121.43, 121.73, 31.26, 31.42],
        [121.80, 121.88, 30.85, 30.92],
        [122.00, 122.10, 30.60, 30.67],
        [122.19, 122.21, 30.10, 30.12],
        [121.71, 122.08, 29.75, 30.00]
    ]
    for item in port_area:
        count_port += traces_df['lng'][
            (traces_df['lng'] >= item[0]) & (traces_df['lng'] <= item[1]) & (traces_df['lat'] >= item[2]) & (
                        traces_df['lat'] <= item[3])].count()
    ts2 = int(time.time())
    info['ts'] = ts2 - ts1

    if count_port > 0 and len(trace_lngs) < 90000:
        return trace_lngs, trace_lats, trace_speeds, trace_ts, trace_weights, info
    else:
        info['error'] = 'not in YRD port'
        return [], [], [], [], [], info


def cluster_dbscan(traces, cluster_eps, cluster_sample):  # 聚类函数
    db = DBSCAN(eps=cluster_eps, min_samples=cluster_sample, algorithm='auto').fit(traces.iloc[:, [0, 1]])
    cluster_lables = db.labels_
    num_clusters = len(set(cluster_lables))
    del db
    return num_clusters, cluster_lables


def classify(df, dict_pollutant, emission_level, oil):  # 此函数旨在对车辆运行模式进行分类并且计算各类占比
    ts1 = int(time.time())
    # 计算a,STP,v,分类
    df['speed'] = df['speed'] * 1000 / 3600
    df['accelerate'] = df['speed'].diff() / 30
    df['time_diff'] = df['timestamp'].diff()
    df = df.fillna(0)
    df['time_diff'] = df.time_diff.map(lambda x: 0 if x > 300 else x)  # 将大于300s的数据替换为0

    df['STP'] = (0.5629625 * df['speed'] + 0.001538425 * df['speed'] * df['speed'] * df['speed'] + load * df[
        'speed'] * (df['accelerate'] + 9.8 * 0.0415)) / 10
    df['rkv'] = pd.cut(df['speed'], [0, 0.44704, 11.176, 22.352, 100], labels=['1', '2', '3', '4'], right=False,
                       include_lowest=True)
    df['rkstp'] = pd.cut(df['STP'], [-90, 0, 3, 6, 9, 12, 18, 24, 30, 90],
                         labels=['1', '2', '3', '4', '5', '6', '7', '8', '9'], right=False, include_lowest=True)
    df['rkv'] = df['rkv'].astype(str)
    df['rkstp'] = df['rkstp'].astype(str)
    df['rk'] = df['rkv'] + df['rkstp']
    df['rk'] = df['rk'].replace(
        {'11': '1', '12': '1', '13': '1', '14': '1', '15': '1', '16': '1', '17': '1', '18': '1', '21': '2', '22': '3',
         '23': '4', '24': '5', '25': '6', '26': '7', '27': '7', '28': '7', '29': '7', '31': '8', '32': '9',
         '33': '10', '34': '11', '35': '12', '36': '13', '37': '14', '38': '15', '39': '16', '41': '17', '42': '17',
         '43': '17', '44': '18', '45': '18', '46': '19', '47': '20', '48': '21', '49': '22'})  # 赋予23种OpMode

    df['rk'] = df['rk'].mask(df['accelerate'] < -0.628, '0')  # 判断OpMode0
    df['dist'] = df['speed'] * df['time_diff'] / 1000
    list_co = []
    list_nox = []
    list_pm = []
    list_hc = []
    for i in df['rk']:
        list_co.append(dict_pollutant['co' + oil][i][emission_level])
        list_nox.append(dict_pollutant['nox' + oil][i][emission_level])
        list_pm.append(dict_pollutant['pm' + oil][i][emission_level])
        list_hc.append(dict_pollutant['hc' + oil][i][emission_level])

    df['co_er'] = list_co
    df['nox_er'] = list_nox
    df['hc_er'] = list_hc
    df['pm_er'] = list_pm
    df['co'] = df['co_er'] * df['time_diff']
    df['pm'] = df['pm_er'] * df['time_diff']
    df['nox'] = df['nox_er'] * df['time_diff']
    df['hc'] = df['hc_er'] * df['time_diff']

    # CO2
    co2_er = dict_pollutant['co2' + oil][emission_level]
    df['co2'] = co2_er * df['dist'] / 1000

    # BC1,BC2
    df['vsp'] = df['speed'] * (1.1 * df['accelerate'] + 9.81 * 0.0415 + 0.132) + 0.000302 * df['speed'] * df['speed'] * \
                df['speed']
    if load < 20:
        if emission_level <= 4:
            df['bc1_er'] = 206 + 0.458 * df['vsp'] + 2.9 * df['vsp'] * df['vsp'] - 0.010 * df['vsp'] * df['vsp'] * df[
                'vsp']
            df['bc2'] = 0.521 * df['pm']
        else:
            df['bc1_er'] = 60.4 - 0.306 * df['vsp'] - 0.051 * df['vsp'] * df['vsp'] + 0.004 * df['vsp'] * df['vsp'] * \
                           df['vsp']
            df['bc2'] = 0.267 * df['pm']

    else:
        if emission_level <= 3:
            df['bc1_er'] = 28.3 + 5.20 * df['vsp'] + 0.194 * df['vsp'] * df['vsp'] - 0.019 * df['vsp'] * df['vsp'] * df[
                'vsp']
            df['bc2'] = 0.588 * df['pm']
        elif emission_level == 4:
            df['bc1_er'] = 122 + 2.84 * df['vsp'] - 0.015 * df['vsp'] * df['vsp'] - 0.00361 * df['vsp'] * df['vsp'] * \
                           df['vsp']
            df['bc2'] = 0.588 * df['pm']
        else:
            df['bc1_er'] = 68.8 + 0.772 * df['vsp'] + 0.015 * df['vsp'] * df['vsp'] - 0.00163 * df['vsp'] * df['vsp'] * \
                           df['vsp']
            df['bc2'] = 0.352 * df['pm']
    df['bc1'] = df['bc1_er'] * df['time_diff'] / 1000000

    return df


# 建立各港口城市相关月排放清单及车流量清单
def grid_pollution_cal(grid_pollution, record_list, trace_lngs, trace_lats, pollution_list, pol_dict):
    for i in record_list:
        for pol in pollution_list:
            if pol_dict[pol][i] > 0:
                tmp_lng = math.floor(trace_lngs[i] * 100) / 100.0
                tmp_lat = math.floor(trace_lats[i] * 100) / 100.0
                if not tmp_lng in grid_pollution[pol]:
                    grid_pollution[pol][tmp_lng] = {}
                if not tmp_lat in grid_pollution[pol][tmp_lng]:
                    grid_pollution[pol][tmp_lng][tmp_lat] = round(pol_dict[pol][i], 9)
                else:
                    grid_pollution[pol][tmp_lng][tmp_lat] += round(pol_dict[pol][i], 9)

    return grid_pollution


# 程序开始

start_group_index = 0
end_group_index = 0
group_index = 0
group_step = 50

month = '201901'

cluster_eps = 0.0005
cluster_sample = 30

#raw_db = 'sinoiov_raw'
#data_db = 'sinoiov_data_%s' % month
#ip = '127.0.0.1'
#username = 'username'
#passwd = 'passwd'
#dbr = easyMySQL(host=ip, user=username, passwd=passwd, db=raw_db)
#dbc = easyMySQL(host=ip, user=username, passwd=passwd, db=data_db)
dbr = r'./测试文件/test.csv'
dbc = r'./测试文件/AIS.csv'
# 排放因子
co_dsl = pd.read_csv(r'./排放因子/柴油CO.csv', index_col=0)
hc_dsl = pd.read_csv(r'./排放因子/柴油HC.csv', index_col=0)
nox_dsl = pd.read_csv(r'./排放因子/柴油NOx.csv', index_col=0)
pm_dsl = pd.read_csv(r'./排放因子/柴油PM2.5.csv', index_col=0)
co_gas = pd.read_csv(r'./排放因子/汽油CO.csv', index_col=0)
hc_gas = pd.read_csv(r'./排放因子/汽油HC.csv', index_col=0)
nox_gas = pd.read_csv(r'./排放因子/汽油NOx.csv', index_col=0)
pm_gas = pd.read_csv(r'./排放因子/汽油PM2.5.csv', index_col=0)
co_oth = pd.read_csv(r'./排放因子/其他CO.csv', index_col=0)
hc_oth = pd.read_csv(r'./排放因子/其他HC.csv', index_col=0)
nox_oth = pd.read_csv(r'./排放因子/其他NOx.csv', index_col=0)
pm_oth = pd.read_csv(r'./排放因子/其他PM2.5.csv', index_col=0)
co2_dsl = {1: 1025, 2: 936, 3: 884, 4: 791, 5: 587.23}
co2_oth = {1: 845, 2: 819, 3: 774, 4: 707, 5: 707}
co2_gas = {1: 845, 2: 819, 3: 774, 4: 707, 5: 707}
dict_oil = {'柴油': 'dsl', '汽油': 'gas', '天然气': 'oth', '电动': 'oth', 'LNG': 'oth', '空值': 'oth', '其他': 'oth',
            "双燃料(同时用两种)": 'oth', 'CNG': 'oth', '混合动力': 'oth'}
dict_emission = dict(国一=1, 国二=2, 国三=3, 国四=4, 国五=5, 国六=5)
dict_pollutant_raw = dict(codsl=co_dsl, hcdsl=hc_dsl, noxdsl=nox_dsl, pmdsl=pm_dsl, cogas=co_gas, hcgas=hc_gas,
                          noxgas=nox_gas, \
                          pmgas=pm_gas, cooth=co_oth, hcoth=hc_oth, noxoth=nox_oth, pmoth=pm_oth, co2dsl=co2_dsl,
                          co2gas=co2_gas, co2oth=co2_oth)

port_list = {
    '上海': 'sh',
    '宁波': 'nb',
    '苏州': 'sz',
    '南京': 'nj',
    '芜湖': 'wh',
    '镇江': 'zj',
    '总体': 'total'
}

pollution_list = ['co', 'hc', 'nox', 'pm', 'co2', 'bc1', 'bc2']

# 读取高速服务区轮廓数据、堆场轮廓数据
service_area_shp = r'./map/shape_service_area_YRD_combine.shp'
service_area = shapefile.Reader(service_area_shp)
area_shp = r'./map/Export_Output_2.shp'  # 换了个堆场名直接是港口名的图层
area = shapefile.Reader(area_shp)
record = area.shapeRecords()

for group_index in range(start_group_index, end_group_index + 1):
    startTime = int(time.time())

    # grid_pollution存储网格排放数据，代表四种污染物的月排放清单
    grid_pollution = {}
    port_efficiency = {}  # 用来统计各港口装卸货时间。
    trans_length = {}  # 用以统计各港口运输距离。
    teu_dict = {}  # 用来统计各港口的teu
    betw_port = []  # 港口间运输，起点 终点，距离
    truck_id = []  # 用以统计所有符合要求的车的id，以对港区集疏运体系车辆情况进行分析
    for key in port_list.keys():
        grid_pollution[key] = {}
        for pol in pollution_list:
            grid_pollution[key][pol] = {}
        port_efficiency[key] = []
        trans_length[key] = []
        teu_dict[key] = [0]

    # 创建结果文件
    print('Generate result files...')
    gridResultFile = u'./result/%s/%s_grid.csv' % (month, group_index)
    fg = open(gridResultFile, 'w+')
    head_row = ['port', 'pollutant', 'lng', 'lat', 'value']
    fg.write(','.join(head_row) + '\n')

    efficiencyResultFile = u'./result/%s/%s_efficiency.csv' % (month, group_index)
    fe = open(efficiencyResultFile, 'w+')
    head_row = ['port', 'time']
    fe.write(','.join(head_row) + '\n')

    lengthResultFile = u'./result/%s/%s_length.csv' % (month, group_index)
    fl = open(lengthResultFile, 'w+')
    head_row = ['port', 'type', 'length']
    fl.write(','.join(head_row) + '\n')

    truckResultFile = u'./result/%s/%s_truck.csv' % (month, group_index)
    ft = open(truckResultFile, 'w+')
    head_row = ['id', 'count']
    ft.write(','.join(head_row) + '\n')

    p2pResultFile = u'./result/%s/%s_port2port.csv' % (month, group_index)
    fp = open(p2pResultFile, 'w+')
    head_row = ['start', 'end', 'length']
    fp.write(','.join(head_row) + '\n')

    teuResultFile = u'./result/%s/%s_teu.csv' % (month, group_index)
    fteu = open(teuResultFile, 'w+')
    head_row = ['port', 'teu']
    fteu.write(','.join(head_row) + '\n')

    start_index = group_index * 10000
    end_index = start_index + group_step

    # 车辆静态数据字典
    print('Read basic car info...')
    car_info = {}
    #dataSql = "SELECT ID,engine_power,fuel,emission FROM car_info WHERE ID BETWEEN %d AND %d" % (start_index, end_index)


    with open(dbr,'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            car_info[int(item['ID'])] = {
                'load': int(item['engine_power']),
                'oil': item['fuel'],
                'oil_level': int(item['emission'])
            }


    print('Start...')
    total_car_port = 0
    for car_sid in range(start_index, end_index):
        if not car_sid in car_info:
            print('car sid: %d, no car info' % car_sid)
            continue

        carStartTime = int(time.time())

        get_data_status = False
        while not get_data_status:
            try:
                trace_lngs, trace_lats, trace_speeds, trace_ts, trace_weights, info = retrieve_trace_db(dbc, car_sid)
                get_data_status = True
            except Exception as e:
                print('Query data fail, try again...')
                pass
        if len(trace_lngs) == 0:
            error_message = info.get('error', '')
            print('sid: %d, error: %s...' % (car_sid, error_message))
            continue

        count_raw = info.get('count_raw', 0)
        count_new = info.get('count_new', 0)

        traces = pd.DataFrame({'lng': trace_lngs, 'lat': trace_lats, 'speed': trace_speeds, 'timestamp': trace_ts})
        print('Start clustering...')
        num_clusters = 0
        dbscan_status = False
        while not dbscan_status:
            try:
                num_clusters, cluster_lables = cluster_dbscan(traces, cluster_eps, cluster_sample)
                dbscan_status = True
            except Exception as e:
                print('DBscan fail, try again...')
                pass

        try:
            load = car_info[car_sid]['load'] / 1000.0
            oil = dict_oil.get(car_info[car_sid]['oil'], 'dsl')
            oil_level = car_info[car_sid]['oil_level']
            emission_level = dict_emission.get(oil_level, 5)

            dict_pollutant = {}
            dict_pollutant['co' + oil] = dict_pollutant_raw['co' + oil].to_dict('dict')
            dict_pollutant['nox' + oil] = dict_pollutant_raw['nox' + oil].to_dict('dict')
            dict_pollutant['pm' + oil] = dict_pollutant_raw['pm' + oil].to_dict('dict')
            dict_pollutant['hc' + oil] = dict_pollutant_raw['hc' + oil].to_dict('dict')
            dict_pollutant['co2' + oil] = dict_pollutant_raw['co2' + oil]

            lngs_center = []
            lats_center = []
            cluster_infos = {}
            for cluster in range(0, num_clusters - 1):
                # 取每一类中点的平均值作为判断坐标
                lng_c = traces['lng'][cluster_lables == cluster].mean()
                lat_c = traces['lat'][cluster_lables == cluster].mean()
                lngs_center.append(lng_c)
                lats_center.append(lat_c)
                cluster_infos[cluster] = [lng_c, lat_c]

            # 按照顺序把驻留点及其统计数据存储在traces_order数组中
            print('process stay point...')
            cluster_infos_filter = {}
            traces_order = []
            prev_cluster = -1
            cluster_count = 0
            total_length = 0
            total_time = 0
            index_list = []
            for i, temp_cluster in enumerate(cluster_lables):
                if i == len(cluster_lables) - 1 and temp_cluster == -1:  # 加了一个最后一个点不在cluster里时把最后一个停留点到终点的数据留下来的判定
                    index_list.append(i)
                    total_length += trace_speeds[i] / 3.6 * 30
                    total_time += 30 * trace_weights[i]
                    traces_order.append([-2, 0, total_length, total_time, index_list])
                else:
                    index_list.append(i)
                    if temp_cluster == -1:
                        total_length += trace_speeds[i] / 3.6 * 30
                        total_time += 30 * trace_weights[i]
                        if not prev_cluster == -1:
                            if cluster_count > cluster_sample:
                                # 记录停留点
                                traces_order.append([prev_cluster, cluster_count, total_length, total_time, index_list])
                                if not prev_cluster in cluster_infos_filter:
                                    cluster_infos_filter[prev_cluster] = [cluster_infos[prev_cluster][0],
                                                                          cluster_infos[prev_cluster][1], False, False]
                                total_length = 0
                                total_time = 0
                                index_list = []
                        cluster_count = 0
                    else:
                        if temp_cluster == prev_cluster:
                            cluster_count += trace_weights[i]
                        else:
                            if not prev_cluster == -1:
                                if cluster_count > cluster_sample:
                                    # 记录停留点
                                    traces_order.append(
                                        [prev_cluster, cluster_count, total_length, total_time, index_list])
                                    if not prev_cluster in cluster_infos_filter:
                                        cluster_infos_filter[prev_cluster] = [cluster_infos[prev_cluster][0],
                                                                              cluster_infos[prev_cluster][1], False,
                                                                              False]
                                    total_length = 0
                                    total_time = 0
                                    index_list = []
                                cluster_count = 1
                    prev_cluster = temp_cluster

            traces_order.append([-1, 0])
        except Exception as e:
            carEndTime = int(time.time())
            tempTime = int(time.time())
            error_message = 'process stay error'
            print('sid: %d, time: %d/%d seconds, raw/new: %d/%d, clusters: %d, error: %s' % (
            car_sid, (carEndTime - carStartTime), (tempTime - startTime), count_raw, count_new, num_clusters,
            error_message))
            continue

        cal_status = False
        a = False
        # 判断是否属于高速服务区、堆场
        print('process stay point judgement...')
        try:
            cal_df = classify(traces, dict_pollutant, emission_level, oil)
            cal_status = True

            for k in cluster_infos_filter.keys():
                cluster_lng = cluster_infos_filter[k][0]
                cluster_lat = cluster_infos_filter[k][1]
                point = [cluster_lng, cluster_lat]
                for j, poly in enumerate(area.shapes()):
                    judge_area = geometry.Point(point).within(geometry.shape(poly))
                    if judge_area:
                        a = True
                        cluster_infos_filter[k][2] = True
                        cluster_infos_filter[k].append(j)
                        break
                for j, poly in enumerate(service_area.shapes()):
                    judge_service = geometry.Point(point).within(geometry.shape(poly))
                    if judge_service:
                        cluster_infos_filter[k][3] = True
                        break
        except Exception as e:
            carEndTime = int(time.time())
            tempTime = int(time.time())
            error_message = 'cal/judge error'
            print('sid: %d, time: %d/%d seconds, raw/new: %d/%d, clusters: %d, error: %s' % (
            car_sid, (carEndTime - carStartTime), (tempTime - startTime), count_raw, count_new, num_clusters,
            error_message))
            continue

        region_dict = {}  # 用来获取符合要求的各港口轨迹点
        for key in port_list.keys():
            region_dict[key] = []

        pol_dict = {}

        # 计算单个集卡车的集装箱数，空载率为28.1%，载重大于40000kg为2teu，否则为1teu
        if car_info[car_sid]['load'] > 40000:
            sin_teu = 2 * (1 - 0.281)
        else:
            sin_teu = 1 * (1 - 0.281)

        count = 0
        if a and cal_status:  # 只在经过港区时才进行如下计算
            try:
                # 将顺序排列的驻留点相邻分类合并，形成最终顺序排列的驻留点数组
                lngs_order = []
                lats_order = []
                temp_cluster = -1
                temp_count = 0
                temp_length = 0
                temp_time = 0
                last_judge = False
                service_label = ''
                tmp_list = []
                between_judge = 0
                for i, temp_item in enumerate(traces_order):
                    if not temp_item[0] < 0:
                        if cluster_infos_filter[temp_item[0]][3]:
                            service_label = 'Service: '
                        else:
                            service_label = 'P: '
                        if temp_item[0] != traces_order[i + 1][
                            0] and service_label != 'Service: ':  # 把休息站的距离和时间叠加到下一个停留点
                            temp_count += temp_item[1]
                            temp_length += temp_item[2] / 1000
                            temp_time += temp_item[3] / 3600
                            cluster_lng = cluster_infos_filter[temp_item[0]][0]
                            cluster_lat = cluster_infos_filter[temp_item[0]][1]
                            point = [cluster_lng, cluster_lat]
                            lngs_order.append(cluster_lng)
                            lats_order.append(cluster_lat)

                            judge = cluster_infos_filter[temp_item[0]][2]
                            judge_service = cluster_infos_filter[temp_item[0]][3]

                            if judge:
                                between_judge += 1
                                if between_judge > 1:
                                    pre_index = cluster_infos_filter[traces_order[i - 1][0]][4]
                                    betw_port.append(
                                        [record[pre_index].record[0], record[index].record[0], temp_length])
                                count += 1
                                index = cluster_infos_filter[temp_item[0]][4]
                                region_dict['总体'] = region_dict['总体'] + tmp_list + temp_item[4]
                                region_dict[record[index].record[0]] = region_dict[record[index].record[0]] + tmp_list + \
                                                                       temp_item[4]
                                teu_dict[record[index].record[0]][0] = teu_dict[record[index].record[0]][
                                                                           0] + sin_teu  # 进港teu计算
                                port_efficiency[record[index].record[0]].append(temp_count / 120.0)
                                trans_length[record[index].record[0]].append(['arrive', temp_length])
                                tmp_list = []
                                print('Arrive port: %s (%.6f, %.6f), stay %.1f hours, distance: %.1f km, time: %.1f hours' % (record[index].record[0], cluster_lng, cluster_lat, temp_count / 120, temp_length, temp_time))
                            else:
                                if last_judge:
                                    between_judge = 0
                                    count += 1
                                    region_dict['总体'] = region_dict['总体'] + tmp_list + temp_item[4]
                                    region_dict[record[index].record[0]] = region_dict[
                                                                               record[index].record[0]] + tmp_list + \
                                                                           temp_item[4]
                                    teu_dict[record[index].record[0]][0] = teu_dict[record[index].record[0]][
                                                                               0] + sin_teu  # 出港teu计算
                                    trans_length[record[index].record[0]].append(['leave', temp_length])
                                    tmp_list = []
                                    print('Leave port: %d (%.6f, %.6f), stay %.1f hours, distance: %.1f km, time: %.1f hours' % (temp_item[0], cluster_lng, cluster_lat, temp_count / 120, temp_length, temp_time))
                                else:
                                    tmp_list = []
                                    print('%s %d (%.6f, %.6f), Stay %.1f hours, distance: %.1f km, time: %.1f hours' % (service_label, temp_item[0], cluster_lng, cluster_lat, temp_count / 120, temp_length, temp_time))

                            temp_count = 0
                            temp_length = 0
                            temp_time = 0
                            last_judge = judge
                        else:
                            # 这里我没有对停留时间进行叠加，是因为休息区的时间不应该加进港区停留时间（即作业时间），但是可能存在连续两个休息区的情况，
                            # 条件判断不好写，而我不研究中间点的停留问题，故忽视
                            temp_count += temp_item[1]
                            temp_length += temp_item[2] / 1000
                            temp_time += temp_item[3] / 3600
                            tmp_list += temp_item[4]

                    elif temp_item[0] == -2:
                        temp_count += temp_item[1]
                        temp_length += temp_item[2] / 1000
                        temp_time += temp_item[3] / 3600
                        print('End: %d (%.6f, %.6f), Stay %.1f hours, distance: %.1f km, time: %.1f hours' % (temp_item[0], cluster_lng, cluster_lat, temp_count / 120, temp_length, temp_time))

                # 这里程序最开始定义了truck_id.最终要保存所有符合要求的车的id以及路程段数，以便计算运载集装箱数
                if not len(region_dict['总体']) == 0:
                    truck_id.append([car_sid, count])

                for pol in pollution_list:
                    pol_dict[pol] = cal_df[pol].values

                # 累加网格数据
                for key in port_list.keys():
                    grid_pollution[key] = grid_pollution_cal(grid_pollution[key], region_dict[key], trace_lngs,
                                                             trace_lats, pollution_list, pol_dict)

            except Exception as e:
                carEndTime = int(time.time())
                tempTime = int(time.time())
                error_message = 'process trace cal error'
                print('sid: %d, time: %d/%d seconds, raw/new: %d/%d, clusters: %d, error: %s' % (
                car_sid, (carEndTime - carStartTime), (tempTime - startTime), count_raw, count_new, num_clusters,
                error_message))
                continue

        carEndTime = int(time.time())
        tempTime = int(time.time())
        if len(region_dict.get('总体', [])) == 0:
            error_message = 'no port'
            print('sid: %d, time: %d/%d seconds, raw/new: %d/%d, clusters: %d, error: %s' % (
            car_sid, (carEndTime - carStartTime), (tempTime - startTime), count_raw, count_new, num_clusters,
            error_message))
        else:
            total_car_port += 1
            print('sid: %d, time: %d/%d seconds, raw/new: %d/%d, clusters: %d, total_count: %d' % (
            car_sid, (carEndTime - carStartTime), (tempTime - startTime), count_raw, count_new, num_clusters, count))

        del trace_lngs, trace_lats, trace_speeds, trace_ts, info, traces, num_clusters, cluster_lables, dict_pollutant, cluster_infos, cluster_infos_filter, region_dict
        gc.collect()

    # 写入数据
    for key in port_list.keys():
        for pol in pollution_list:
            for lng_key in grid_pollution[key][pol].keys():
                for lat_key in grid_pollution[key][pol][lng_key].keys():
                    try:
                        temp_row = [key, pol, str(lng_key), str(lat_key),
                                    str(grid_pollution[key][pol][lng_key][lat_key])]
                        fg.write(','.join(temp_row) + '\n')
                    except Exception as e:
                        pass

    for key in port_list.keys():
        for value in port_efficiency[key]:
            try:
                temp_row = [key, ('%.3f' % value)]
                fe.write(','.join(temp_row) + '\n')
            except Exception as e:
                pass

    for key in port_list.keys():
        for tmp_row in trans_length[key]:
            try:
                temp_row = [key, tmp_row[0], str(tmp_row[1])]
                fl.write(','.join(temp_row) + '\n')
            except Exception as e:
                pass

    for tmp_row in truck_id:
        try:
            temp_row = [str(tmp_row[0]), str(tmp_row[1])]
            ft.write(','.join(temp_row) + '\n')
        except Exception as e:
            pass

    for tmp_row in betw_port:
        try:
            temp_row = [tmp_row[0], tmp_row[1], str(tmp_row[2])]
            fp.write(','.join(temp_row) + '\n')
        except Exception as e:
            pass

    for key in port_list.keys():
        for value in teu_dict[key]:
            try:
                temp_row = [key, ('%.3f' % value)]
                fteu.write(','.join(temp_row) + '\n')
            except Exception as e:
                pass
    fg.close()
    fe.close()
    fl.close()
    ft.close()
    fp.close()
    fteu.close()

    endTime = int(time.time())
    print('Group: %d, sid range: %d to %d, total car port: %d, time: %d seconds' % (group_index, start_index, end_index-1, total_car_port, (endTime - startTime)))