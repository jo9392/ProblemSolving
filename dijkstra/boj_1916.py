import heapq
import sys


input = sys.stdin.readline
n = int(input())
m = int(input())
INF = 100000*1000 + 1

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, [0, start])

    while(q):
        dist, now = heapq.heappop(q)
        if (distance[now] < dist):
            continue

        for city, cost in graph[now]:
            cost += dist
            if distance[city] > cost:   # 갱신하려는 값이 더 작으면
                distance[city] = cost   # 갱신하기
                heapq.heappush(q, [cost, city])

distance = [INF]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])

start, end = map(int, input().split())
dijkstra(start)

print(distance[end])
