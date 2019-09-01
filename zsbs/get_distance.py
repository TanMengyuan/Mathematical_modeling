import numpy as np
from math import *


EARTH_RADIUS = 6378.137  # earth radius(km)
IS_PROVINCE = True
IS_INTERNET_INDEX = False

pop_index = 3 if IS_PROVINCE else 2
pop_index = 4 if IS_INTERNET_INDEX else pop_index

print(pop_index)

pos = [
    ['00', '哈尔滨', [126.63333, 45.75, 10.635971, 38.312224, 2.1129]],
    ['01', '乌鲁木齐', [87.68333, 43.76667, 3.11028, 21.813334, 1.1478]],
    ['02', '北京&天津', [116.80834, 39.525, 32.550224, 32.550224, 9.3263]],
    ['03', '西安', [108.95, 34.26667, 8.467837, 37.327378, 4.2335]],
    ['04', '郑州', [113.65, 34.76667, 8.626505, 94.023567, 4.9192]],
    ['05', '上海',	[121.43333,	34.5, 23.019148, 23.019148, 11.4235]],
    ['06', '成都',	[104.06667,	30.66667, 14.047625, 80.4182, 8.2939]],
    ['07', '重庆',	[106.45, 29.56667, 28.8462, 28.8462, 6.4946]],
    ['08', '武汉',	[114.31667, 30.51667, 9.785392, 57.23774, 7.6144]],
    ['09', '拉萨',	[91, 29.6, 0.559423, 3.002166, 0.2526]],
    ['10', '昆明',	[102.73333, 25.05, 6.432, 45.966, 2.8970]],
    ['11', '广州&深圳',	[113.65, 22.89167, 23.058738, 104.303132, 23.8720]]
]   # [id, name, [longitude, latitude, population, province_population, internet_index]]

def calcDistance(pos1, pos2):
    Lat_A, Lng_A, Lat_B, Lng_B = pos1[2][1], pos1[2][0], pos2[2][1], pos2[2][0]
    radLat1 = radians(Lat_A)
    radLat2 = radians(Lat_B)
    a = radLat1 - radLat2
    b = radians(Lng_A) - radians(Lng_B)

    s = 2 * asin(sqrt(pow(sin(a / 2), 2) + cos(radLat1) * cos(radLat2) * pow(sin(b / 2), 2)))
    s = round(s * EARTH_RADIUS, 4)
    return s

def get_dis(pos):
    result = []
    for start in range(len(pos)):
        tmp = []
        for end in range(len(pos)):
            # if start == end:
            #     continue
            distance = calcDistance(pos[start], pos[end])
            if distance == 0:
                cap = 0
            elif distance < 600:
                cap = 32
            elif distance < 1200:
                cap = 16
            elif distance < 3000:
                cap = 8
            else:
                cap = 0
            pop = round(np.sqrt(pos[start][2][pop_index] * pos[end][2][pop_index]), 4)
            value = cap * pop
            tmp.append((pos[start][0], pos[end][0], distance, cap, pop, value))
        result.append(tmp)
    return result


dis = get_dis(pos)  # [start_id, end_id, distance, cap, pop, value]

print(dis)

# save_path = r'E:\sola\NJUPT\数学建模\正式比赛\q2-2_value_2.xls'
# import xlrd
# import xlwt
# f = xlwt.Workbook()
# sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
# n = 1
# for i in range(len(pos)):
#     name = pos[i][0] + '-' + pos[i][1]
#     sheet1.write(0, n, name)
#     sheet1.write(n, 0, name)
#     n += 1
#
# for i in range(len(dis)):
#     for j in range(len(dis[i])):
#         sheet1.write(i + 1, j + 1, dis[i][j][5])
#
# f.save(save_path)
# print('save successful on ', save_path)

value = []
for i in range(len(dis)):
    for j in range(len(dis[i])):
        value.append([dis[i][j][5], dis[i][j][3], dis[i][j][0], dis[i][j][1]])
rank_value = sorted(value)[:-66:-2]
sum_value = 0
for i in range(len(rank_value)):
    sum_value += rank_value[i][0]

for line in rank_value:
    print(line)
print(sum_value)