def solution(s):
    stack = []
    for i in s:
        if stack == []:
            stack.append(i)
        elif stack[-1] == '(' and i == ')':
            stack.pop()
        else:
            stack.append(i)
    
    if stack: return False 
    else: return True