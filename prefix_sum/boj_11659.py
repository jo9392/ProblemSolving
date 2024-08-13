import sys

input = sys.stdin.readline

num_cnt, op_cnt = map(int, input().split())
num_list = list(map(int, input().split()))
sum_list = [0]*(num_cnt+2)
sum_list[1] = num_list[0]
for i in range(num_cnt):
    sum_list[i+1] = sum_list[i] + num_list[i]
for _ in range(op_cnt):
    a, b = map(int, input().split())
    print(sum_list[b]-sum_list[a-1])