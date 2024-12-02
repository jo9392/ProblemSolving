import sys

input = sys.stdin.readline

n = int(input())

def back_tracking(temp_num, end_num, sum, expression, pos_num):
    if temp_num == end_num+1:
        sum += pos_num
        if sum == 0:
            answer_list.append(expression)
        return
    else:
        # 공백
        if pos_num < 0:
            blank_pos_num = pos_num*10 - temp_num
        else:
            blank_pos_num = pos_num*10 + temp_num
        back_tracking(temp_num+1, end_num, sum, expression+' '+str(temp_num), blank_pos_num)
        
        # 더하기
        back_tracking(temp_num+1, end_num, sum+pos_num, expression+'+'+str(temp_num), temp_num)
        
        # 빼기
        back_tracking(temp_num+1, end_num, sum+pos_num, expression+'-'+str(temp_num), (-1)*temp_num)

    
for i in range(n):
    test_case = int(input())
    answer_list = []
    back_tracking(2, test_case, 0, '1', 1, )
    for answer in answer_list:
        print(answer)
    if i != (n-1):
        print("")