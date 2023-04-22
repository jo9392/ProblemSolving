import sys
input = sys.stdin.readline
global b_image, label_image, m, n, neighbor8, num_region, label_num


def read_image():
    global m, n, b_image
    m, n = map(int, input().split())
    if (m, n) == (0,0):
        return m, n
    binary_list = []
    for _ in range(m):
        line = [int(i) for i in input().strip('\n')]
        binary_list.append(line)
    b_image = binary_list
    return m, n

def save_image(file_name):
    global label_image
    f = open(file_name, 'w')
    f.write(str(label_num-1)+"\n")
    for l in label_image:
        f.write(" ".join(str(i) for i in l))
        f.write("\n")
    f.close()

def label_with_BT():    #라벨링 함수
    global b_image, label_image, m, n, num_region, label_num
    max_size = 1000 # 임의의 가능 개체 수 max 지정
    label_image = []
    for j in range(m): label_image.append([0]*(n))
    num_region = [0]*(max_size)   #개체의 개수 세는 리스트
    label_num=1                     #현재 추적 중인 개체의 라벨
    for i in range(1,m-1):     #네 면의 한 줄씩은 띄워놓고 사용
        for j in range(1, n-1):
            if label_image[i][j] == 0:  #label image에서 픽셀이 0일때
                cur_p = b_image[i][j]   #현재 탐색중인 픽셀 지정
                if cur_p == 1: # object를 만났을 때 탐색 시작
                    ref_p1 = label_image[i][j-1]
                    ref_p2 = label_image[i-1][j-1]
                    # if ref_p1 > 1 : # p1에 개체가 있으면 propagation
                    #     num_region[ref_p1] += 1
                    #     label_image[i][j] = ref_p1
                    # if ref_p1==0 and ref_p2 >= 2: # p1은 비었고 p2에만 개체가 있으면 hole
                    #     num_region[ref_p2] += 1
                    #     label_image[i][j] = ref_p2
                    #     boundary_tracing(i, j, ref_p2, "backward")
                    if ref_p1 == 0 and ref_p2 == 0: ## 새로운 개체 탐색, region start
                        label_num += 1
                        num_region[label_num] += 1
                        label_image[i][j] = label_num
                        boundary_tracing(i, j, label_num, "foreward")

def read_neighbor8(y, x): #neighbor8 배열에 현재 neighbor를 저장하는 함수
    global neighbor8, b_image

    neighbor8 = []
    pos_change = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
    for p in pos_change:
        neighbor8.append(b_image[y+p[0]][x+p[1]])

def cal_coord(add_o, y, x): #현재 위치가 x, y인 상태에서 add_o만큼 옮겨주는 함수
    pos_change = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
    y += pos_change[add_o][0]
    x += pos_change[add_o][1]
    return y, x

def boundary_tracing(y, x, label, tag):
    global neighbor8, label_image, num_region
    # neighbor8 배열은 x,y 주변 8픽셀값이 시계방향 순서대로 리스트 형태로 들어가있어야 함
    if tag == 'foreward': cur_orient = 0
    else: cur_orient = 6
    end_x = x
    end_y = y

    first_flag = False
    while(y!=end_y or x!=end_x or not first_flag):
        read_neighbor8(y, x)
        start_o = (8+cur_orient-2) % 8

        stop_flag = False
        for i in range(8):
            add_o = (start_o + i) % 8
            if neighbor8[add_o] != 0:
                stop_flag = True
                break

        if stop_flag:   #특정 방향에서 1 이상인 픽셀을 발견했다면
            y, x = cal_coord(add_o, y, x)    # 방향을 계산해서 새로운 픽셀로 옮겨가기
            cur_orient = add_o          # 현재 방향 갱신
            if label_image[y][x] == 0:
                num_region[label] += 1
                label_image[y][x] = label
        else: break

        first_flag = True


if __name__ == "__main__":
    case_num = 0
    while(True):
        case_num += 1
        m, n = read_image()
        if (m, n) == (0, 0):
            break
        label_with_BT()
        answer = ""
        for n in num_region[2:]:
            if n > 5:
                answer += str(n) + " "
            if n == 0:
                break
        save_image(f"output{case_num}")
        print("Case ", case_num)
        if answer == "":
            print("no objects found")
        else:
            print(answer[:-1])