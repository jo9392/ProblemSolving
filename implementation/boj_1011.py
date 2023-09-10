import sys

input = sys.stdin.readline

def solution(k):
    num_cnt = 1
    num_left = 1
    num_right = 1
    while(not num_left <= k <= num_right):
        num_cnt += 1
        limit = (num_cnt-1)//2+1
        num_left = num_right+1
        num_right += limit
    print(num_cnt)


n = int(input())
for i in range(n):
    p, q = map(int, input().split())
    k = q-p
    solution(k)