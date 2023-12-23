import sys
import itertools


input = sys.stdin.readline
n, m = map(int, input().split())
list_1 = list()
list_2 = list()
for i in range(n):
    temp_matrix = list(map(int, input().split()))
    for j in range(n):
        if temp_matrix[j] == 1:
            list_1.append([i,j])
        elif temp_matrix[j] == 2:
            list_2.append([i,j])

nCr = list(itertools.combinations(list_2, m))

total = 100*2500
for index2 in nCr:
    temp_total = 0
    for [x1, y1] in list_1:
        temp_cost = 100*2500
        for [x2, y2] in index2:
            temp_cost = min(temp_cost, abs(x1-x2)+abs(y1-y2))
        temp_total += temp_cost
    total = min(total, temp_total)
print(total)
