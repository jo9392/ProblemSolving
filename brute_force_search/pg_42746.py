def solution(numbers):
    str_list = [str(n) for n in numbers]
    str_list = sorted(str_list, key=lambda x:x*3, reverse=True)        
    answer = str(int("".join(str_list)))
    return answer