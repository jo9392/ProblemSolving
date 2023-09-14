import sys
from itertools import combinations

input = sys.stdin.readline
length, cnt = map(int, input().split())
c_list = list(input().split())
all_list = c_list.copy()
aeious = ['a','e','i','o','u']
input_aeiou = []
for a in aeious:
    if a in c_list:
        input_aeiou.append(a)
        c_list.remove(a)

answer = set()
combi = list(combinations(c_list, 2))

for i in range(len(input_aeiou)):
    for j in combi:
        a, b = (j)
        temp_all = all_list.copy()
        temp_all.remove(input_aeiou[i])
        temp_all.remove(a)
        temp_all.remove(b)
        temp_answer = input_aeiou[i] + a + b
        ttemp_combi = list(combinations(temp_all, length-3))
        for t in ttemp_combi:
            ttemp_answer = temp_answer
            for k in t:
                ttemp_answer += k
            ttemp_answer = "".join(sorted(ttemp_answer))
            answer.add(ttemp_answer)

answer = list(answer)
answer.sort()
for a in answer:
    print(a)