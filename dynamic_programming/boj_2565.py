import sys

input = sys.stdin.readline
n = int(input())
line = {}
for i in range(n):
    a, b = map(int, input().split())
    line[a] = b
b_line = sorted(line.items())
b_line.items
len_b = len(b_line)

dp_max = [1] * len_b
dp_min = [1] * len_b
for i in range(len_b):
    for j in range(i):
        if dp_max[i] >= dp_max[j]:
            dp_max[i] = max(dp_max[i], dp_max[j]+1)
        if dp_min[i] <= dp_min[j]:
            dp_min[i] = max(dp_min[i], dp_min[j]+1)

print(min(n-max(dp_max), n-max(dp_min)))
