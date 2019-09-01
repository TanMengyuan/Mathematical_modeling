import numpy as np
from math import *

EARTH_RADIUS = 6378.137  # earth radius(km)

pos = [
    ['00', '哈尔滨', [126.63333, 45.75, 10.635971, 1]],
    ['01', '乌鲁木齐', [87.68333, 43.76667, 3.11028, 1]],
    ['02', '北京&天津', [116.80834, 39.525, 32.550224, 1]],
    ['03', '西安', [108.95, 34.26667, 8.467837, 1]],
    ['04', '郑州', [113.65, 34.76667, 8.626505, 1]],
    ['05', '上海',	[121.43333,	34.5, 23.019148, 1]],
    ['06', '成都',	[104.06667,	30.66667, 14.047625, 1]],
    ['07', '重庆',	[106.45, 29.56667, 28.8462, 1]],
    ['08', '武汉',	[114.31667, 30.51667, 9.785392, 1]],
    ['09', '拉萨',	[91, 29.6, 0.559423, 1]],
    ['10', '昆明',	[102.73333, 25.05, 6.432, 1]],
    ['11', '广州&深圳',	[113.65, 22.89167, 23.058738, 1]]
]   # [id, name, [longitude, latitude, population, weight]]

def calcDistance(pos1, pos2):
    Lat_A, Lng_A, Lat_B, Lng_B = pos1[1], pos1[0], pos2[1], pos2[0]
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
            if start == end:
                continue
            distance = calcDistance(pos[start][2], pos[end][2])
            if distance < 600:
                v = 32
            elif distance < 1200:
                v = 16
            elif distance < 3000:
                v = 8
            else:
                v = 0
            pop = round(np.sqrt(pos[start][2][2] * pos[end][2][2]), 4)
            value = v * pop
            tmp.append((pos[start][0], pos[end][0], distance, v, pop, value))
        result.append(tmp)
    return result

distance = get_dis(pos)
# dis is [start_id, end_id, distance, capacity, population, net_value]
value = []
for i in range(len(distance)):
    for j in range(len(distance[i])):
        value.append((distance[i][j][5], distance[i][j][3], distance[i][j][0], distance[i][j][1]))
rank_value = sorted(value)[::-2]
print(rank_value)


