import sys

input = sys.stdin.readline

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

operation = []
for _ in range(m):
    x, y = list(map(int, input().split()))
    operation.append([x, y-1])


def cloud_move(cloud, direct, cnt):
    for i in range(len(cloud)):
        x, y = cloud[i]
        if direct == (1 or 2 or 8):
            y -= cnt
        if direct == (4 or 5 or 6):
            y += cnt
        if direct == (2 or 3 or 4):
            x -= cnt
        if direct == (6 or 7 or 8):
            x += cnt
    
        if x >= n:
            x -= n
        elif x < 0:
            x += n
        if y >= n:
            y -= n
        elif y < 0:
            y += n
        
        cloud[i] = [x, y]
    print(cloud)
    return cloud
        
def rain(cloud):
    for x, y in cloud:
        grid[x][y] += 1

def water_copy(cloud):
    move_x = [1,1,-1,-1]
    move_y = [1,-1,1,-1]
    for i in range(n):
        for j in range(n):
            if [i,j] in cloud:
                continue
            move_pos = []
            for k in range(4):
                x, y = i+move_x[k], j+move_y[k]
                if 0 <= x < n and 0 <= y < n:
                    grid[i][j] += 1

def cloud_generate():
    cloud = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 2:
                cloud.append([i,j])
                grid[i][j] -= 2
    return cloud

# 초기 구름 생성
cloud = [[n-1, 0], [n-1,1],[n-2,0],[n-2,1]]

for i in range(m):
    for k in range(n):
        print(grid[k])
    print("------------------")
    # 구름 이동
    direct, cnt = operation[i]
    print(cloud)
    print("-------구름-----------")
    cloud = cloud_move(cloud, direct, cnt)
    print(cloud)
    print("-------구름-----------")
    # 물 +1
    rain(cloud)
    for k in range(n):
        print(grid[k])
    print("------------------")
    # 물복사버그
    water_copy(cloud)
    # 구름 생성
    cloud = cloud_generate()
    

answer = sum(sum(grid, [])) + len(cloud)*2
print(answer)
