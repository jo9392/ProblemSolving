import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

n = int(input())
graph_key = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph_key[a].append(b)
    graph_key[b].append(a)

root_node = [0]*n
root_node[0] = -1

def dfs(node):
    for child in graph_key[node]:
        if root_node[child-1] != 0:
            continue
        root_node[child-1] = node
        dfs(child)

dfs(1)
for r in root_node[1:]:
    print(r)