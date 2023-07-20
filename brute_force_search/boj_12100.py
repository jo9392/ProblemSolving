#list에 인덱스로 값 추가는 insert(index, value)
import sys
from collections import deque
import copy
input = sys.stdin.readline

def move_left(n, origin_map):
    copy_map = copy.deepcopy(origin_map)
    #왼쪽 정렬
    for i in range(n):
        copy_map[i] = [k for k in copy_map[i] if k not in {0}]
        temp_len = len(copy_map[i])
        for j in range(n-temp_len):
            copy_map[i].append(0)
    #합치기
    for i in range(n):
        for j in range(1, n):
            if copy_map[i][j] == copy_map[i][j-1]:
                copy_map[i][j-1] *= 2
                copy_map[i].pop(j)
                copy_map[i].append(0)

    return copy_map

def move_right(n, origin_map):
    # 180도 회전
    origin_map = turn_left(n, origin_map)
    origin_map = turn_left(n, origin_map)
    # 왼쪽 이동
    origin_map = move_left(n, origin_map)
    # 180도 회전
    origin_map = turn_left(n, origin_map)
    origin_map = turn_left(n, origin_map)
    return origin_map

def move_up(n, origin_map):
    #왼쪽으로 90도 회전
    origin_map = turn_left(n, origin_map)
    #왼쪽 이동
    origin_map = move_left(n, origin_map)
    #오른쪽으로 90도 회전
    origin_map = turn_right(n, origin_map)
    return origin_map

def move_down(n, origin_map):
    # 오른쪽으로 90도 회전
    origin_map = turn_right(n, origin_map)
    # 왼쪽 이동
    origin_map = move_left(n, origin_map)
    # 왼쪽으로 90도 회전
    origin_map = turn_left(n, origin_map)
    return origin_map

def turn_left(n, origin_map):
    turned_map = list(map(list, zip(*origin_map)))[::-1]
    return turned_map

def turn_right(n, origin_map):
    turned_map = list(map(list, zip(*origin_map[::-1])))
    return turned_map

n = int(input())
map_2048 = list()
for i in range(n):
    temp_line = list(map(int, input().split()))
    map_2048.append(temp_line)
map_dq = deque()
map_dq.append((map_2048, 0))
answer = 0

while(map_dq):
    temp_map, cnt = map_dq.popleft()
    for i in temp_map:
        if cnt < 5:
            cnt += 1
            left_moved = move_left(n, temp_map)
            right_moved = move_right(n, temp_map)
            up_moved = move_up(n, temp_map)
            down_moved = move_down(n, temp_map)
            answer = max(answer,max(sum(left_moved+right_moved+up_moved+down_moved, [])))

            map_dq.append((left_moved, cnt))
            map_dq.append((right_moved, cnt))
            map_dq.append((up_moved, cnt))
            map_dq.append((down_moved, cnt))

print(answer)