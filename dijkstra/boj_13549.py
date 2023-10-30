import heapq


me, target = map(int, input().split())
hq = []
INF = 200000
max_size = max(me, target)
dp = [INF for i in range(max_size*2+1)]
dp[me] = 0
heapq.heappush(hq, [0, me])

while(hq):
    cost, pos = heapq.heappop(hq)
    if dp[pos] < cost:
        continue

    if 0 <= pos-1 <= max_size*2 and dp[pos-1] > cost+1:
        dp[pos-1] = cost+1
        heapq.heappush(hq, [cost+1, pos-1])

    if 0 <= pos+1 <= max_size*2 and dp[pos+1] > cost+1:
        dp[pos+1] = cost+1
        heapq.heappush(hq, [cost+1, pos+1])

    if 0 <= pos*2 <= max_size*2 and dp[pos*2] > cost:
        dp[pos*2] = cost
        heapq.heappush(hq, [cost, pos*2])

print(dp[target])