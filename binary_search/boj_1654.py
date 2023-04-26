import sys
input = sys.stdin.readline
k, n = map(int, input().split())
input_line_list = []
for _ in range(k): input_line_list.append(int(input()))

optimum = int(sum(input_line_list) / n)

left = 1
right = optimum

def can_be_mid(n, input_line_list, mid):
    line_cnt = 0
    for i in input_line_list:
        line_cnt += int(i/mid)
    if line_cnt >= n:
        return True
    else:
        return False

while(True):
    mid = int((left+right)/2)
    if can_be_mid(n, input_line_list, mid):
        left = mid+1
    else:
        right = mid-1
    if left > right : break

mid = int((left+right)/2)
print(mid)