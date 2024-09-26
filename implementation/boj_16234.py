import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

n, l, r = map(int, input().split())

table = list()
for i in range(n):
    table.append(list(map(int, input().split())))

visited = [[0]*n for _ in range(n)]
answer = 0

def chain_lands(pos, sum, chain_list):
    global table, visited
    (pos_x, pos_y) = pos
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    temp_value = table[pos_x][pos_y]
    n = len(table)
    for i in range(4):
        next_x = pos_x + dx[i]
        next_y = pos_y + dy[i]
        if 0<=next_x<n and 0<=next_y<n:
            next_value = table[next_x][next_y]
            if visited[next_x][next_y] == 0 and l <= abs(temp_value - next_value) <= r:
                visited[pos_x][pos_y] = 1
                visited[next_x][next_y] = 1
                sum += next_value
                chain_list.append((next_x, next_y))
                chain_list, sum = chain_lands((next_x, next_y), sum, chain_list)

    return chain_list, sum


def make_average(chain_list, sum):
    global table
    avg = sum // len(chain_list)
    for x, y in chain_list:
        table[x][y] = avg


while(True):
    visited = [[0]*n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                chain_list, sum = chain_lands((i,j), table[i][j], [(i,j)])
                if len(chain_list) > 1:
                    flag = True
                make_average(chain_list, sum)
    
    if flag:
        answer += 1
    else:
        break

print(answer)