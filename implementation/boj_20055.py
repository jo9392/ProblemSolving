import sys
from collections import deque

input = sys.stdin.readline
length, stop_cnt = map(int, input().split())
durability = deque(map(int, input().split()))

answer = 0
dura_zero_cnt = 0
for d in durability:
    if d == 0:
        dura_zero_cnt += 1
is_robot = deque([0]*(2*length))
while(True):
    answer += 1
    # 한 칸 회전
    temp_dura = durability.pop()
    durability.appendleft(temp_dura)
    temp_robot = is_robot.pop()
    is_robot.appendleft(temp_robot)
    is_robot[length] = 0

    # 한 칸 이동
    is_robot[length-1] = 0
    for i in range(length-2, -1, -1):
        if not is_robot[i+1] and durability[i+1] and is_robot[i]:
            is_robot[i] = 0
            is_robot[i+1] = 1
            durability[i+1] -= 1
            if durability[i+1] == 0:
                dura_zero_cnt += 1

    # 올리는 위치 로봇 올리기
    if durability[0]:
        is_robot[0] = 1
        durability[0] -= 1
        if durability[0] == 0:
            dura_zero_cnt += 1

    #내구도 검사            
    if dura_zero_cnt >= stop_cnt:
        break


print(answer)