global maze_map
global temp_pos

def save_map():
    global maze_map
    input_val = list(map(int, input().split()))
    x, y = map(int, input_val[0:2])
    input_map = input_val[2:]
    print(input_map)
    maze_map = []
    for i in range(x):
        maze_map.append([int(j) for j in str(input_map[i])])
    # list_map = list(map(int, input()))
    # maze_map = []
    # for i in range(0, len(list_map), y):
    #     maze_map.append(list_map[i:i + y])
    return (x-1, y-1)

def move_position(move):
    global maze_map
    global temp_pos
    maze_map[temp_pos[0]][temp_pos[1]] = 0
    if move == 'down':
        temp_pos = (temp_pos[0]+1, temp_pos[1])
    elif move == 'right':
        temp_pos = (temp_pos[0], temp_pos[1]+1)
    elif move == 'up':
        temp_pos = (temp_pos[0]-1, temp_pos[1])
    elif move == 'left':
        temp_pos = (temp_pos[0], temp_pos[1]-1)
    else:
        print('wrong element!')

def index_error_flag(pos):
    try:
        maze_map[pos[0]][pos[1]]
        return 0
    except:
        return 1
    return false

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    global maze_map
    global temp_pos
    des_pos = save_map()
    temp_pos = (0,0)
    count = 0
    print(maze_map)
    while(temp_pos != des_pos):
        if (not index_error_flag((temp_pos[0]+1,temp_pos[1]))) and maze_map[temp_pos[0]+1][temp_pos[1]] == 1:
            move_position('down')
            print("down\n")
            count+=1
        elif (not index_error_flag((temp_pos[0],temp_pos[1]+1))) and maze_map[temp_pos[0]][temp_pos[1]+1] == 1:
            move_position('right')
            print("right\n")
            count += 1
        elif (not index_error_flag((temp_pos[0]-1,temp_pos[1]))) and maze_map[temp_pos[0]-1][temp_pos[1]] == 1:
            move_position('up')
            print("up\n")
            count += 1
        elif (not index_error_flag((temp_pos[0],temp_pos[1]-1))) and maze_map[temp_pos[0]][temp_pos[1]-1] == 1:
            move_position('left')
            print("left\n")
            count += 1
        else :
            print("something gone wrong!\n")
            break
    print((temp_pos[0]+1, temp_pos[1]+1), count+1)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
