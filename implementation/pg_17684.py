# 재귀함수를 작성할 땐 return 원함수()라고 작성해줘야 none type return을 막을 수 있다
# for문에서 i에 특정 값을 더하는 방식으로는 pass가 안 된다
def search_str_len(msg, i, max_len, A_dict):
    search_str = "".join(msg[i:i+max_len])
    if search_str not in A_dict:
        return search_str_len(msg, i, max_len-1, A_dict)
    else:
        return search_str, max_len

def solution(msg):
    answer = []
    A_dict = {chr(i + 64): i for i in range(1, 27)}
    dict_len = 26
    max_len = 1
    pass_num = 0
    for i in range(len(msg)):
        if i<pass_num:
            continue
        search_str, str_len = search_str_len(msg, i, max_len, A_dict)
        answer.append(A_dict[search_str])
        if i + str_len == len(msg):
            break
        else:
            add_str = "".join(msg[i:i + str_len + 1])
            A_dict[add_str] = dict_len + 1
            dict_len += 1
            max_len = max(max_len, len(add_str))
        pass_num = i + str_len
    return answer