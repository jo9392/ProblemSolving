import sys
input = sys.stdin.readline

global gear
gear = []
turn = []
for i in range(4):
    gear.append([input().strip(), 0])

n = int(input())
for i in range(n):
    turn.append(list(map(int, input().split())))

# 회전 -> 시작 인덱스(12시 인덱스)의 위치 이동
# 시계방향 -> index -= 1, 반시계방향 -> index += 1
# 맞닿는 부분 -> (왼쪽)index - 2, (오른쪽)index + 2

def gear_turn(num, wise, dir):
    global gear
    temp_num = 7 if wise == 1 else 1
    post_index = gear[num-1][1]
    gear[num-1][1] = (gear[num-1][1]+temp_num) % 8  # 시작 인덱스 업데이트
    left_index = (post_index + 6) % 8
    right_index = (post_index + 2) % 8
    # 왼쪽 기어 바꾸기
    if num != 1 and dir != 1:
        if gear[num-1][0][left_index] != gear[num-2][0][(gear[num-2][1]+2)%8]:
            gear_turn(num-1, wise*(-1), -1)
    # 오른쪽 기어 바꾸기
    if num != 4 and dir != -1:
        if gear[num-1][0][right_index] != gear[num][0][(gear[num][1]+6)%8]:
            gear_turn(num+1, wise*(-1), 1)

for num, wise in turn:
    gear_turn(num, wise, 0)

answer = 0
if gear[0][0][gear[0][1]] == '1':
    answer += 1
if gear[1][0][gear[1][1]] == '1':
    answer += 2
if gear[2][0][gear[2][1]] == '1':
    answer += 4
if gear[3][0][gear[3][1]] == '1':
    answer += 8

print(answer)