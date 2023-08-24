import sys

input = sys.stdin.readline

n = int(input())
table_list = list()
for i in range(n):
    table_list.append(list(map(int, input().split())))
cnt_1 =
def pos_value(pos):
    global table_list
    return table_list[pos[0]][pos[1]]
def revise_value(pos, value):
    global table_list
    table_list[pos[0]][pos[1]] = value

def label_with_BT():
    global table_list,
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while(True):    #table에 1이 없을때까지
        temp_dir_idx = 0
        temp_dir = dir[temp_dir_idx]
        temp_pos = [0, 0]
        temp_idx = 2
        while(True):    #시작점 탐색
            if pos_value(temp_pos) == 1:   #시작점 찾았으면 break
                break
            temp_pos = [temp_pos[0]+temp_dir[0], temp_pos[1]+temp_dir[1]]   #위치 이동

            if temp_pos[0] >= n:
                temp_pos = [0, temp_pos[1]+1]
            elif temp_pos[0] < 0:
                temp_pos = [0, temp_pos[1]-1]
            if temp_pos[1] >= n:
                temp_pos = [temp_pos[0]+1, 0]
            elif temp_pos[1] < 0:
                temp_pos = [temp_pos[0]-1, 0]

        start_pos = temp_pos
        temp_pos = [start_pos[0]+temp_dir[0], start_pos[1]+temp_dir[1]] #시작지점에서 한 칸 이동
        revise_value(temp_pos, temp_idx)
        while(temp_pos != start_pos):   #경계추적 시작
            next_pos = [temp_pos[0]+temp_dir[0], temp_pos[1]+temp_dir[1]]
            if pos_value(next_pos) == 1:
                temp_pos = next_pos
                revise_value(temp_pos, temp_idx)
            else:
                temp_dir_idx = (temp_dir_idx + 1) % 4   #방향 변경
                temp_dir = dir[temp_dir_idx]