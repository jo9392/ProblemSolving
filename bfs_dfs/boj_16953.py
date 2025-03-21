import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())

num_dq = deque()
num_dq.append([a,0])
real_answer = -1
while(num_dq):
    temp, answer = num_dq.popleft()
    if temp == b:
        real_answer = answer+1
        break
    if temp*2 <= b:
        num_dq.append([temp*2, answer+1])
    if temp*10+1 <= b:
        num_dq.append([temp*10+1, answer+1])

print(real_answer)