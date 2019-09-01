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

rank_value = [[644.1632, 32, '07', '06'], [536.2208, 32, '04', '02'], [500.128, 32, '07', '03'],
              [437.968, 16, '02', '05'], [412.6496, 16, '07', '11'], [297.704, 16, '00', '02'],
              [294.0064, 32, '04', '08'], [285.552, 16, '08', '02'], [273.4976, 32, '04', '03'],
              [268.8144, 16, '07', '08'], [265.6336, 16, '03', '02'], [252.3952, 16, '07', '04'],
              [245.1384, 8, '07', '02'], [217.9408, 16, '07', '10'], [80.4944, 8, '02', '01'],
              [34.1376, 8, '09', '02']]

# for s in rank_value:
#     if s[2] > s[3]:
#         tmp = s[2]
#         s[2] = s[3]
#         s[3] = tmp
# rank_value = sorted(rank_value, key=lambda x: x[2])
#
# path_dic = {}
# for s in rank_value:
#     path_dic.setdefault(s[2], []).append(s[3])
#     path_dic.setdefault(s[3], []).append(s[2])
#
# print(path_dic)


# def get_one_path(start, end, tmp, path):
#     if len(tmp) > 3:
#         return tmp, path, False
#     if start in tmp:
#         return tmp, path, False
#     tmp.append(start)
#     start_next = path_dic[start]
#     print(tmp)
#     if end in start_next:
#         tmp.append(end)
#         path.append(tmp)
#         return [], path, True
#     for a in start_next:
#         tmp, path, is_end = get_one_path(a, end, tmp, path)
#         # print('show', a, end, tmp, path)
#         # print(is_end)
#
#         # print(tmp)
#
#     return path
#
# def find_path(point_start_id, point_end_id):
#     result = []
#     tmp = []
#     value = 0
#     Flag = False
#     for s in rank_value:
#         if point_start_id in s and point_end_id in s:
#             return [point_start_id, point_end_id]
#
#
#
#     return result
#
# for start in range(len(pos)):
#     distribute = []
#     point_start_id = pos[start][0]
#     for end in range(len(pos)):
#         if start == end:
#             continue
#         # distribute the flux
#         sta_pop = pos[start][2][2]
#         end_pop = pos[end][2][2]
#         line_pop = min(sta_pop, end_pop)
#         distribute.append(line_pop)
#
#         # find minimum net value path
#         point_end_id = pos[end][0]
#         tmp = find_path(point_start_id, point_end_id)
#
#
#     sum_cap = sum(distribute)
#     per_cap = [i / sum_cap for i in distribute]
#     # print(per_cap)
