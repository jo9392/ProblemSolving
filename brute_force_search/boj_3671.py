import sys
from itertools import permutations
import math

input = sys.stdin.readline

n = int(input())

range_num = 9999999
# 소수 배열
prime = [True for _ in range(range_num+1)]
prime[0]=False
prime[1] = False
for i in range(2, int(math.sqrt(range_num)+1)):
    if prime[i]:
        j = 2
        while i*j <= range_num:
            prime[i*j] = False
            j += 1

for _ in range(n):
    target_num = str(input().strip())

    nPr = []
    for i in range(1, len(target_num)+1):
        nPr += permutations(target_num, i)
    nPr = list(set(nPr))

    answer = 0
    for num in nPr:
        num = "".join(num)
        if num[0] != '0':
            num = int(num)
            if prime[num]:
                answer += 1

    print(answer)