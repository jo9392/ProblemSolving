# bin() : 10진수 -> 2진수 표현
def one_to_binary(s, zero_cnt):
    # x의 1의 개수를 2진법으로 표현하는 연산
    s0 = s.replace('0','')
    zero_cnt += len(s) - len(s0)
    s0 = bin(len(s0))
    return s0[2:], zero_cnt

def solution(s):
    zero_cnt = 0
    run_cnt = 0
    while(s!='1'):
        run_cnt += 1
        s, zero_cnt = one_to_binary(s, zero_cnt)
    answer = [run_cnt, zero_cnt]
    return answer