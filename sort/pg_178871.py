def solution(players, callings):
    num_list = [i for i in range(len(players))]
    players_dict = dict(zip(players, num_list))
    numbers_dict = dict(zip(num_list, players))
    for temp_player in callings:
        temp_num = players_dict[temp_player]
        fore_num = temp_num - 1
        foreward_player = numbers_dict[fore_num]

        players_dict[foreward_player], players_dict[temp_player] = temp_num, fore_num
        numbers_dict[temp_num], numbers_dict[fore_num] = foreward_player, temp_player

    answer = list(numbers_dict.values())
    return answer