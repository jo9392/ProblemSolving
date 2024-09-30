import sys

n, m, x, y, cnt = map(int, input().split())

map_table = list()
dice_num = [0,0,0,0,0,0]
for _ in range(n):
    map_table.append(list(map(int, input().split())))

move_order = list(map(int, input().split()))

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
temp_x = x
temp_y = y
def turn_dice(dice_num, move):
    new_dice_num = [0,0,0,0,0,0]
    if move == 1:
        new_dice_num = [dice_num[4],
                        dice_num[1],
                         dice_num[5],
                         dice_num[3],
                         dice_num[2],
                         dice_num[0]]
    elif move == 2:
        new_dice_num = [dice_num[5],
                        dice_num[1],
                         dice_num[4],
                         dice_num[3],
                         dice_num[0],
                         dice_num[2]]
    elif move == 3:
        new_dice_num = [dice_num[1],
                        dice_num[2],
                         dice_num[3],
                         dice_num[0],
                         dice_num[4],
                         dice_num[5]]
    elif move == 4:
        new_dice_num = [dice_num[3],
                        dice_num[0],
                         dice_num[1],
                         dice_num[2],
                         dice_num[4],
                         dice_num[5]]
    return new_dice_num

for move in move_order:
    next_x = temp_x + dx[move]
    next_y = temp_y + dy[move]
    if 0 <= next_x < n and 0 <= next_y < m:
        temp_x = next_x
        temp_y = next_y
        dice_num = turn_dice(dice_num, move)
        if map_table[temp_x][temp_y] != 0:
            dice_num[2] = map_table[temp_x][temp_y]
            map_table[temp_x][temp_y] = 0
        else:
            map_table[temp_x][temp_y] = dice_num[2]
        print(dice_num[0])
    else:
        pass