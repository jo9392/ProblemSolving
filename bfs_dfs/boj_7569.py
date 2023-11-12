import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().split())
tomato_list = list()
for i in range(h):
    tomato_list.append([])
    for j in range(n):
        tomato_list[i].append(list(map(int, input().split())))   # 1은 익은 토마토, 0은 안익은 토마토, -1은 빈 칸

fucking_tomato = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato_list[i][j][k] == 1:
                fucking_tomato.append([i,j,k])
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

while(fucking_tomato):
    i, j, k = fucking_tomato.popleft()
    for d in range(6):
        di = i+dx[d]
        dj = j+dy[d]
        dk = k+dz[d]
        if 0<=di<h and 0<=dj<n and 0<=dk<m and tomato_list[di][dj][dk] == 0:
            fucking_tomato.append([di,dj,dk])
            tomato_list[di][dj][dk] = tomato_list[i][j][k] + 1

answer = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            answer = max(answer, tomato_list[i][j][k])
            if tomato_list[i][j][k] == 0:
                answer = -1
                break
        if answer == -1:
            break
    if answer == -1:
        break

if answer != -1:
    answer -= 1
print(answer)