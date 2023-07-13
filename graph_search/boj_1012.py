# 최대 재귀 깊이 재설정 : sys.setrecursionlimit(num)
# 리스트에서 값 제거 : remove(value)

import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

def solution(cabbage_cnt, cabbage_pos):
    bug_cnt = 0

    while cabbage_pos:
        temp_pos = cabbage_pos.pop()
        bug_cnt += 1
        temp_list = list([temp_pos])
        temp_pos, cabbage_pos, bug_cnt, temp_list = connect(temp_pos, cabbage_pos, bug_cnt, temp_list)

    return bug_cnt
def connect(temp_pos, cabbage_pos, bug_cnt, temp_list):
    pos = [[1,0], [0,1], [0,-1], [-1,0]]
    for p in pos:
        next_pos = [temp_pos[0] + p[0], temp_pos[1] + p[1]]
        if next_pos in cabbage_pos:
            temp_list.append(next_pos)
            cabbage_pos.remove(next_pos)
            next_pos, cabbage_pos, bug_cnt, temp_list = connect(next_pos, cabbage_pos, bug_cnt, temp_list)

    return next_pos, cabbage_pos, bug_cnt, temp_list

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        w, h, cabbage_cnt = map(int,(input().split()))
        cabbage_pos = list()
        for j in range(cabbage_cnt):
            cabbage_pos.append(list(map(int,(input().split()))))
        print(solution(cabbage_cnt, cabbage_pos))
