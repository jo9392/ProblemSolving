# 다시 풀 것
def solution(s):
    stack = []
    for i in s:
        if stack == []:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    
    if stack == []:
        return 1
    else:
        return 0