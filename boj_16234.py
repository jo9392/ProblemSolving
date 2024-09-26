# 인접한 숫자가 L~R 차이면 평균내서 합치기
# 인구이동 안 일어날 때까지 반복

import sys

input = sys.stdin.readline

n, l, r = map(int, input().split())

table = list()
for i in range(n):
    table.append(list(map(int, input().split())))

visited = [[0]*n for _ in range(n)]


def chain_lands(pos):
    # 매번 상하좌우 탐색해서 넘어가는데
    # 전역 변수 sum에다가 지금 숫자를 넣어줘야함
    # 전역 변수 count 값도 1 더해줘야함
    chain_list = []

    return chain_list


for i in range(n):
    for j in range(n):
        if visited[i][j] == 1:
            continue
        else:
            visited[i][j] = 1
            chain_lands((i,j))
            # 여기서 sum 값 초기화 해줘야함
            # 여기서 평균내서 값 적용해줘야함

        
            
