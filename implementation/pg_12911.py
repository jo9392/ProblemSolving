# 10->2진수 : bin()
# string 개수 세기 : .count('')
def solution(n):
    bin_n = bin(n)
    one = bin_n.count('1')
    while(True):
        n += 1
        if one == bin(n).count('1'):
            break
            
    return n