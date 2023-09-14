import sys
from collections import deque

input = sys.stdin.readline
length, cnt = map(int, input().split())
c_list = list(input().split())
aeious = ['a','e','i','o','u']
input_aeiou = []
for a in aeious:
    if a in c_list:
        input_aeiou.append(a)
        c_list.remove(a)

answer = []
for i in range(len(input_aeiou)):
    temp_answer = ''
    temp_answer += input_aeiou[i]
    for j in range(len(c_list)):
        temp_answer += #랜덤으로 두 개 선택