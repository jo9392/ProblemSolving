import sys

input = sys.stdin.readline
n = int(input())
color_cost = list()
color_cost.append([0,0,0])
for i in range(n):
    temp_cost = list(map(int, input().split()))
    color_cost.append(temp_cost)

cost_list = list()
cost_list.append([0, 0, 0])
for i in range(1, len(color_cost)):
    cost_list.append([min(cost_list[i-1][1],cost_list[i-1][2])+color_cost[i][0],
                    min(cost_list[i-1][0],cost_list[i-1][2])+color_cost[i][1],
                    min(cost_list[i-1][0],cost_list[i-1][1])+color_cost[i][2]])
cost = min(cost_list.pop())
print(cost)