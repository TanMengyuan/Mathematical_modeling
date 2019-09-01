from collections import defaultdict
from heapq import *
import numpy as np
from math import *

IS_MIN_CONNECT = True
IS_PROVINCE = False
IS_INTERNET_INDEX = False
NEED_SAVE_XLS = False
NUM_OF_CONNECT = 16

pop_index = 3 if IS_PROVINCE else 2
pop_index = 4 if IS_INTERNET_INDEX else pop_index

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
rank_value16 = [[644.1632, 32, '07', '06'], [536.2208, 32, '04', '02'], [500.128, 32, '07', '03'],
              [437.968, 16, '02', '05'], [412.6496, 16, '07', '11'], [297.704, 16, '00', '02'],
              [294.0064, 32, '04', '08'], [285.552, 16, '08', '02'], [273.4976, 32, '04', '03'],
              [268.8144, 16, '07', '08'], [265.6336, 16, '03', '02'], [252.3952, 16, '07', '04'],
              [245.1384, 8, '07', '02'], [217.9408, 16, '07', '10'], [80.4944, 8, '02', '01'],
              [34.1376, 8, '09', '02']]
rank_value16_prov = [[2347.52, 32, '08', '04'], [1895.7536, 32, '04', '03'], [1770.2944, 32, '04', '02'],
                     [1541.2448, 32, '07', '06'], [1391.2832, 16, '06', '04'], [1236.2608, 16, '11', '08'],
                     [1107.8656, 16, '11', '10'], [1085.5216, 16, '08', '06'], [1050.0448, 32, '07', '03'],
                     [972.7824, 16, '10', '06'], [877.6336, 16, '11', '07'], [876.6192, 16, '06', '03'],
                     [565.0224, 16, '02', '00'], [744.36, 16, '05', '04'], [362.3008, 8, '04', '01'],
                     [141.5648, 8, '11', '09']]
min_connect = [[644.1632, 32, '07', '06'], [536.2208, 32, '04', '02'], [500.128, 32, '07', '03'],
               [437.968, 16, '02', '05'], [412.6496, 16, '07', '11'], [297.704, 16, '00', '02'],
               [294.0064, 32, '04', '08'], [273.4976, 32, '04', '03'],[217.9408, 16, '07', '10'],
               [80.4944, 8, '02', '01'], [34.1376, 8, '09', '02']]
min_connect_prov = [[2347.52, 32, '08', '04'], [1895.7536, 32, '04', '03'], [1770.2944, 32, '04', '02'],
                     [1541.2448, 32, '07', '06'], [1391.2832, 16, '06', '04'], [1236.2608, 16, '11', '08'],
                     [1107.8656, 16, '11', '10'], [744.36, 16, '05', '04'], [565.0224, 16, '02', '00'],
                     [362.3008, 8, '04', '01'], [141.5648, 8, '11', '09']]
min_connect_inter = [[234.8576, 32, '07', '06'], [216.7456, 32, '04', '02'], [215.7152, 16, '11', '08'],
                     [199.224, 16, '11', '07'], [195.8464, 32, '08', '04'], [167.7952, 32, '07', '03'],
                     [165.1488, 16, '05', '02'], [133.0576, 16, '11', '10'], [71.0256, 16, '02', '00'],
                     [26.1744, 8, '02', '01'], [19.6448, 8, '11', '09']]
if IS_MIN_CONNECT and not IS_PROVINCE:
    value_list = min_connect
elif IS_MIN_CONNECT and IS_PROVINCE:
    value_list = min_connect_prov
elif not IS_MIN_CONNECT and IS_PROVINCE:
    value_list = rank_value16_prov
else:
    value_list = rank_value16

if IS_INTERNET_INDEX:
    value_list = min_connect_inter



def dijkstra_raw(edges, from_node, to_node):
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))
    q, seen = [(0, from_node, ())], set()
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == to_node:
                return cost, path
            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost + c, v2, path))
    return float("inf"), []

def dijkstra(edges, from_node, to_node):
    len_shortest_path = -1
    ret_path = []
    length, path_queue = dijkstra_raw(edges, from_node, to_node)
    if len(path_queue) > 0:
        len_shortest_path = length  ## 1. Get the length firstly;
        ## 2. Decompose the path_queue, to get the passing nodes in the shortest path.
        left = path_queue[0]
        ret_path.append(left)  ## 2.1 Record the destination node firstly;
        right = path_queue[1]
        while len(right) > 0:
            left = right[0]
            ret_path.append(left)  ## 2.2 Record other nodes, till the source-node.
            right = right[1]
        ret_path.reverse()  ## 3. Reverse the list finally, to make it be normal sequence.
    return len_shortest_path, ret_path

def get_edges(value_list):
    edges = []
    for i in range(len(value_list)):
        edges.append((value_list[i][2], value_list[i][3], value_list[i][0]))
        edges.append((value_list[i][3], value_list[i][2], value_list[i][0]))

    return edges

def get_all_path(edges, pos_list):
    all_path = []
    for start in range(len(pos_list)):
        from_node = pos_list[start][0]
        tmp = []
        for end in range(len(pos_list)):
            # if start == end:
            #     continue
            to_node = pos_list[end][0]
            min_value, Shortest_path = dijkstra(edges, from_node, to_node)
            tmp.append([from_node, to_node, round(min_value, 4), Shortest_path])
        all_path.append(tmp)

    return all_path

edges = get_edges(value_list)
all_path = get_all_path(edges, pos)
# print('all_path')
# for line in all_path:
#     print(line)
# [[from, to, sum_value, shortest_path]] every city connected to each others



def get_distribute(pos, ratio):
    all_cap = []    # [cap_of_city1, cap_of_city2, ... ,cap_of_cityn]
    for i in range(len(pos)):
        id = pos[i][0]
        sum_cap = 0
        for j in range(len(value_list)):
            if id in value_list[j]:
                sum_cap += value_list[j][1]
        all_cap.append(round(sum_cap, 4))
    # print(all_cap)
    distribute = []
    for start in range(len(pos)):
        tmp = []
        tmp_value = all_cap[start]
        for end in range(len(pos)):
            if start == end:
                tmp.append(0)
                continue
            # distribute the flux
            sta_pop = pos[start][2][pop_index]
            end_pop = pos[end][2][pop_index]
            # calculate the line_pop
            line_pop = np.sqrt(sta_pop * end_pop)
            tmp.append(line_pop)
        sum_cap = sum(tmp)
        per_cap = [round((i / sum_cap) * ratio * tmp_value, 4) for i in tmp]
        distribute.append(per_cap)
    # get the minimum cap between two city
    for i in range(len(distribute)):
        for j in range(len(distribute[i])):
            distribute[i][j] = min(distribute[i][j], distribute[j][i])
    return distribute
# [[cap"00 to 00", cap"00 to 01", ... , cap"00 to 11"],
# [cap"01 to 00", cap"01 to 01", ... , cap"01 to 11"], [ ... ], ... ]
# min(cap"i to j", cap"j to i)


# get cap of every line
def get_cap(distribute):
    path_dic = {}
    for i in range(len(distribute)):
        for j in range(len(distribute[i])):
            cap = distribute[i][j]
            path = all_path[i][j][3]
            for k in range(len(path) - 1):
                if path[k] > path[k + 1]:
                    a, b = path[k + 1], path[k]
                else:
                    a, b = path[k], path[k + 1]
                line = a + '-' + b
                if line in path_dic.keys():
                    path_dic[line] += cap
                else:
                    path_dic[line] = cap

    cap_dic = {}
    for i in range(len(value_list)):
        if value_list[i][2] > value_list[i][3]:
            a, b = value_list[i][3], value_list[i][2]
        else:
            a, b = value_list[i][2], value_list[i][3]
        line = a + '-' + b
        cap = value_list[i][1]
        cap_dic[line] = cap

    gap_dic = {}
    for line in cap_dic.keys():
        if line in path_dic.keys():
            gap_dic[line] = path_dic[line] - cap_dic[line]
        else:
            gap_dic[line] = - cap_dic[line]

    return path_dic, cap_dic, gap_dic


ratio, dic = 1, {}
Flag = True
# find the max amp can be satisfy
for amp in reversed(range(1, 200)):
    amp /= 100
    # print('amp', amp)
    dis_tmp = get_distribute(pos, amp)
    path_dic_tmp, cap_dic_tmp, gap_dic_tmp = get_cap(dis_tmp)
    count = 0
    for key in gap_dic_tmp.keys():
        if gap_dic_tmp[key] > 0:
            n = (gap_dic_tmp[key] // 1) // cap_dic_tmp[key] + 1
            count += n
    if count <= NUM_OF_CONNECT - len(value_list):
        dic = gap_dic_tmp
        ratio = amp
        print('information')
        for key in gap_dic_tmp.keys():
            n = (gap_dic_tmp[key] // 1) // cap_dic_tmp[key] + 1
            remain = round(n * cap_dic_tmp[key] - gap_dic_tmp[key], 4)
            print(key, round(path_dic_tmp[key], 4), cap_dic_tmp[key], round(gap_dic_tmp[key], 4), n, remain)
        break

# print(ratio, dic)
dis = get_distribute(pos, ratio)
path_dic, cap_dic, gap_dic = get_cap(dis)
save_list = []
for key in gap_dic.keys():
    n = (gap_dic[key] // 1) // cap_dic[key] + 1
    remain = round(n * cap_dic[key] - gap_dic[key], 4)
    save_list.append([key, round(path_dic[key], 4), cap_dic[key], round(gap_dic[key], 4), n, remain])

# print(ratio)
# for line in dis:
#     print(line)






if NEED_SAVE_XLS:
    # ==================== save module =================================
    import xlrd
    import xlwt

    save_path = r'E:\sola\NJUPT\数学建模\正式比赛\q2-3_cap_1_33_internet_index.xls'
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)

    # save title
    n = 1
    for i in range(len(pos)):
        name = pos[i][0] + '-' + pos[i][1]
        sheet1.write(0, n, name)
        sheet1.write(n, 0, name)
        n += 1

    # # save cap remain
    # for i in range(len(save_list)):
    #     for j in range(len(save_list[i])):
    #         sheet1.write(i, j, save_list[i][j])
    # sheet1.write(len(save_list) + 1, 0, r'说明：下面信息分别为：”起点“-”终点“	  分配给该线路的流量   	 原本线路最大容量		超出的流量（负值表示未超出）		需要增加n条线路		增加线路后多出的流量')

    # # save cap
    for i in range(len(dis)):
        for j in range(len(dis[i])):
            sheet1.write(i + 1, j + 1, dis[i][j])

    # # save path
    # for i in range(len(all_path)):
    #     for j in range(len(all_path[i])):
    #         sheet1.write(i + 1, j + 1, '-'.join(all_path[i][j][3]))

    f.save(save_path)
    print('save successful on ', save_path)






