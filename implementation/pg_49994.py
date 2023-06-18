def solution(dirs):
    pos_s = set()
    dir_dict = {'U': [0, 1], 'D': [0, -1], 'R': [1, 0], 'L': [-1, 0]}
    temp_pos = [0, 0]
    for d in dirs:
        temp_move = dir_dict[d]
        next_pos_x = temp_pos[0] + temp_move[0]
        next_pos_y = temp_pos[1] + temp_move[1]
        if next_pos_x > 5:
            next_pos_x = 5
        if next_pos_y > 5:
            next_pos_y = 5
        if next_pos_x < -5:
            next_pos_x = -5
        if next_pos_y < -5:
            next_pos_y = -5
        if temp_pos != [next_pos_x, next_pos_y]:
            pos_s.add((next_pos_x, next_pos_y, temp_pos[0], temp_pos[1]))
            pos_s.add((temp_pos[0], temp_pos[1], next_pos_x, next_pos_y))
            temp_pos = [next_pos_x, next_pos_y]

    answer = len(pos_s) / 2
    return answer