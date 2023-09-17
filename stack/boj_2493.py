import sys


input = sys.stdin.readline
n = int(input())
tower_list = list(map(int, input().split()))
answer = [0 for _ in range(n)]
stack = []

for i in range(n):
    while stack:
        if stack[-1][1] > tower_list[i]:
            answer[i] = stack[-1][0]+1
            break
        else:
            stack.pop()
    stack.append([i, tower_list[i]])

print(str(answer)[1:-1].replace(',',''))