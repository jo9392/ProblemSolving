# M개의 묶음으로 숫자의 합 분배, 숫자 합이 최대한 비슷하도록
# 숫자는 연속되어야 함

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lecture = list(map(int, input().split()))

lf = max(lecture)
rt = sum(lecture)

def calculate(mid):
    bluray_cnt = m-1
    temp = mid
    for length in lecture:
        if temp-length >=0: # 현재 블루레이에 추가할 수 있으면
            temp -= length
        elif bluray_cnt>0: # 블루레이 새거 꺼낼 수 있으면
            bluray_cnt-=1
            temp = mid - length
        else:
            return False
    return True

while(lf <= rt):
    mid = (lf+rt)//2
    if calculate(mid):
        rt = mid - 1
    else:
        lf = mid + 1

print(lf)
