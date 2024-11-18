import sys

input = sys.stdin.readline

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

operation = []
for _ in range(m):
    x, y = list(map(int, input().split()))
    operation.append([x, y])


def cloud_move(cloud, direct, cnt):
    cnt = cnt % n
    for i in range(len(cloud)):

        x, y = cloud[i]
        if direct == 1 or direct == 2 or direct == 8:
            y -= cnt
        if direct == 4 or direct == 5 or direct == 6:
            y += cnt
        if direct == 2 or direct == 3 or direct == 4:
            x -= cnt
        if direct == 6 or direct == 7 or direct == 8:
            x += cnt

        if x >= n:
            x = x%n
        elif x < 0:
            x += n
        if y >= n:
            y = y%n
        elif y < 0:
            y += n

        cloud[i] = (x, y)

    return cloud
        
def rain(cloud):
    for x, y in cloud:
        grid[x][y] += 1

def water_copy(cloud):
    move_x = [1,1,-1,-1]
    move_y = [1,-1,1,-1]
    for x, y in cloud:
        for k in range(4):
            next_x, next_y = x+move_x[k], y+move_y[k]
            if 0 <= next_x < n and 0 <= next_y < n and grid[next_x][next_y]>0:
                grid[x][y] += 1

def cloud_generate(cloud):
    new_cloud = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 2:
                new_cloud.append((i,j))
    new_cloud = list(set(new_cloud) - set(cloud))
    for x, y in new_cloud:
        grid[x][y] -= 2
    return new_cloud

# 초기 구름 생성
cloud = [(n-1, 0), (n-1,1),(n-2,0),(n-2,1)]

for i in range(m):
    # 구름 이동
    direct, cnt = operation[i]
    cloud = cloud_move(cloud, direct, cnt)
    # 물 +1
    rain(cloud)
    # 물복사버그
    water_copy(cloud)
    # 구름 생성
    cloud = cloud_generate(cloud)

answer = sum(sum(grid, []))
print(answer)