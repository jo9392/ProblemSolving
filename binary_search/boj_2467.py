import sys

input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))

left_answer = 0
right_answer = 0
answer = float("INF")

for i in range(n-1): # 왼쪽 용액 찾기
    temp_liquid = liquid[i]
    left = i+1
    right = n-1
    while(left <= right):
        mid = (left+right)//2
        mix_value = temp_liquid + liquid[mid]
        if abs(mix_value) < answer: # 정답 갱신이 될 때
            answer = abs(mix_value)
            left_answer = temp_liquid
            right_answer = liquid[mid]

            if mix_value == 0:
                break
        if mix_value < 0: # 합이 음수면 범위 올리기
            left = mid + 1
        elif mix_value > 0 :
            right = mid - 1

print(left_answer, right_answer)
