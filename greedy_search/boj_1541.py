# -가 나올 때부터 다음 -가 나올때까지를 괄호로 묶어서 계산하는 문제
import sys
from collections import deque

input = sys.stdin.readline
input_str = input()
input_q = deque(input_str)
mid_q = deque('(')
while(input_q):
    temp_q = input_q.popleft()
    if '0'<=temp_q<='9':
        if type(mid_q[-1]) == int:
            mid_q.append(mid_q.pop()*10 + int(temp_q))
        else:
            mid_q.append(int(temp_q))
    elif temp_q == '-':
        mid_q.append('-(')
    else:
        mid_q.append('+')

answer = 0
minus_flag = False
while(mid_q):
    temp_q = mid_q.popleft()
    if type(temp_q) == int:
        if minus_flag == False:
            answer += temp_q
        else:
            answer -= temp_q
    elif temp_q == '-(':
        minus_flag = True
print(answer)
