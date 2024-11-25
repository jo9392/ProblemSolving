import sys

input = sys.stdin.readline

n, m = map(int, input().split())
book_pos = list(map(int, input().split()))

plus_pos = []
minus_pos = []
for pos in book_pos:
    if pos <= 0:
        minus_pos.append(pos*(-1))
    else:
        plus_pos.append(pos)
plus_pos.sort()
minus_pos.sort()

work_queue = []
while(plus_pos):
    work_queue.append(plus_pos.pop())
    for i in range(m-1):
        if len(plus_pos)>0:
            plus_pos.pop()

while(minus_pos):
    work_queue.append(minus_pos.pop())
    for i in range(m-1):
        if len(minus_pos)>0:
            minus_pos.pop()

answer = 0
work_queue.sort()
answer += work_queue.pop()
answer += sum(work_queue)*2
print(answer)