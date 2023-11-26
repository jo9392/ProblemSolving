# union-find 알고리즘
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
set_list = list(i for i in range(n+1))

def find(x):
    y = set_list[x]
    if y != set_list[y]:
        return find(y)
    else:
        return y

for i in range(m):
    instruction, a, b = list(map(int, input().split()))
    root_a = find(a)
    root_b = find(b)
    if instruction == 0:
        if root_a < root_b:
            set_list[root_a] = root_b
        else:
            set_list[root_b] = root_a
    else:
        if root_a == root_b:  # a, b가 같은 집합에 들어가 있을 때
            print('YES\n')
        else:
            print('NO\n')