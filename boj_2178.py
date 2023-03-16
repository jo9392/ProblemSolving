global maze_map
from collections import deque

def save_map():
    global maze_map
    x, y = map(int, input().split())
    maze_map = []
    for i in range(x):
        maze_map.append([int(j) for j in input()])
    return (x-1, y-1)


if __name__ == '__main__':
    global maze_map
    des_pos = save_map()
    count = 0
    dq = deque()
    dq.append([(0,0), count])
    pos_change = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while(dq):
        temp_queue = dq.popleft()
        temp_pos = temp_queue[0]
        if temp_pos == des_pos:
            print(temp_queue[1]+1)
            break
        for i in pos_change:
            next_pos = tuple(sum(elem) for elem in zip(temp_pos, i))
            if 0<= next_pos[0] <= des_pos[0] and 0 <= next_pos[1] <= des_pos[1] and maze_map[next_pos[0]][next_pos[1]] == 1:
                maze_map[next_pos[0]][next_pos[1]] = 0
                dq.append([next_pos, temp_queue[1]+1])