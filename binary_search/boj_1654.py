import sys
input = sys.stdin.readline
k, n = map(int, input().split())
init_line_list = []
for _ in range(k): init_line_list.append(int(input()))

optimum = int(sum(init_line_list) / n)
