# def solution(number, k):
#     num_list = [int(n) for n in number]
#     temp_k = k
#     answer = ''
#     while (temp_k > 0 and num_list):
#         if temp_k == len(num_list):
#             num_list = []
#             break
#         max_num = max(num_list[:temp_k + 1])
#         temp_index = num_list[:temp_k + 1].index(max_num)
#         num_list = num_list[temp_index + 1:].copy()
#         temp_k -= temp_index
#         answer += str(max_num)
#
#     answer += "".join([str(n) for n in num_list])
#
#     return answer


def solution(number, k):
    answer_list = list(number[0])

    for n in number[1:]:
        while answer_list and answer_list[-1] < n and k > 0:
            answer_list.pop()
            k -= 1
        answer_list.append(n)

    return "".join(answer_list) if not k else "".join(answer_list[:-k])