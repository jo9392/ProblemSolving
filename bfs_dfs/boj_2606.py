import sys

input = sys.stdin.readline
computer_cnt = int(input())
computer_list = []

for i in range(int(input())):
    (x, y) = map(int, input().split())
    computer_list.append((x, y))

visited = [0 for i in range(len(computer_list))]

virus_list = [1]
virus_set = []

while(virus_list):
    temp_com = virus_list.pop() #temp_com과 이어져있는 컴퓨터 찾기
    for i in range(len(computer_list)):
        if temp_com in computer_list[i] and visited[i] == 0:    #방문한 적 없고 temp_com과 이어져 있으면 리스트에 추가
            if temp_com == computer_list[i][0]:
                virus_list.append(computer_list[i][1])
                virus_set.append(computer_list[i][1])
            else:
                virus_list.append(computer_list[i][0])
                virus_set.append(computer_list[i][0])
            visited[i] += 1

virus_set = set(virus_set)
print(len(virus_set))
