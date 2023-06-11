def solution(record):
    answer = []
    id_name_dic = dict()
    for r in record:
        if r[0] == 'E' or r[0] == 'C':
            temp_r = r.split()
            id_name_dic[temp_r[1]] = temp_r[2]
    for r in record:
        if r[0] == 'E':
            temp_r = r.split()
            user_name = id_name_dic[temp_r[1]]
            answer.append(user_name + "님이 들어왔습니다.")
        elif r[0] == 'L':
            temp_r = r.split()
            user_name = id_name_dic[temp_r[1]]
            answer.append(user_name + "님이 나갔습니다.")

    return answer