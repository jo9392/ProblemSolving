import sys
import heapq


input = sys.stdin.readline

n = int(input())
time = []
for _ in range(n):
    time.append(list(map(int,input().split())))
time.sort(key=lambda x : (x[0],x[1]))

schedule = [time[0][1]]
for i in range(1,n):
    if schedule[0] <= time[i][0]:   # 스케줄 합칠 수 있으면
        heapq.heappop(schedule)
    heapq.heappush(schedule, time[i][1])    #끝나는 시간 갱신

print(len(schedule))