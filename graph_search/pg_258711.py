# 정점 찾기 -> 어느것에서부터도 연결되어있지 않고, 무언가로 연결되어 있기만 한 점
# 그 중에서 가장 연결이 많이 되어있는 점을 찾기
# in은 없고 out만 존재하는 정점
# in_dict로 a로 들어오는 정점들 정리
# out_dict로 a에서 뻗어나가는 정점들 정리
import sys
limit_number = 1000000
sys.setrecursionlimit(limit_number)
from collections import defaultdict
in_dict = defaultdict(list)
out_dict = defaultdict(list)

def find_types(start_node, temp_node):
    out_cnt = len(out_dict[temp_node])
    if out_cnt == 0:
        return "stick"
    elif out_cnt == 2:
        return "eight"
    elif start_node == out_dict[temp_node][0]:
        return "donut"
    else:
        return find_types(start_node, out_dict[temp_node][0])


def solution(edges):
    for a, b in edges:
        in_dict[b].append(a)
        out_dict[a].append(b)

    in_dict_list = list(in_dict.keys())
    out_dict_list = [item[0] for item in sorted(out_dict.items(), key=lambda item: len(item[1]), reverse=True)]

    #정점 찾기
    for o in out_dict_list:
        if o not in in_dict_list:
            s_node = o
            break

    stick = donut = eight = 0
    for n in out_dict[s_node]:
        types = find_types(n, n)
        if types == 'stick':
            stick += 1
        elif types == 'donut':
            donut += 1
        elif types == 'eight':
            eight += 1
    
    answer = [s_node, donut, stick, eight]
    return answer