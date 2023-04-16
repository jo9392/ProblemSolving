import sys
input = sys.stdin.readline
global land_height_list, n, m

n, m, having_block = map(int, input().split())
land_height_list = []
for _ in range(n):
    land_height = list(map(int, input().split()))
    for l in land_height:
        land_height_list.append(l)

def calculate_cost(k):
    global land_height_list
    cost = 0
    for l in land_height_list:
        if l-k >=0:
            cost += (l-k)*2
        else:
            cost -= (l-k)
    return cost

def find_k():
    global land_height_list
    temp_k = int(sum(land_height_list) / len(land_height_list))
    temp_cost = calculate_cost(temp_k)
    past_cost = calculate_cost(temp_k-1)
    pos_change = 1
    if past_cost <= temp_cost:
        pos_change *= (-1)
    while(True):
        temp_k += pos_change
        past_cost = temp_cost
        temp_cost = calculate_cost(temp_k)
        if past_cost < temp_cost:
            temp_k -= pos_change
            break
        elif past_cost == temp_cost:
            pos_change = 1
            temp_k += pos_change
    return temp_k

def is_it_possible_k(k):
    global land_height_list
    sum = 0
    for l in land_height_list: sum += l-k
    if sum+having_block < 0:
        return False
    else:
        return True


if __name__ == "__main__":
    k = find_k()
    if is_it_possible_k(k):
        print(calculate_cost(k), k)
    else:
        cost_list = []
        gap = 0
        while(True):
            gap += 1
            if is_it_possible_k(k+gap) or is_it_possible_k(k-gap):
                break

        if is_it_possible_k(k + gap): cost_list.append([calculate_cost(k+gap), k+gap])
        if is_it_possible_k(k - gap) and k-gap >= 0: cost_list.append([calculate_cost(k - gap), k - gap])

        cost_list = sorted(cost_list, key=lambda x:(x[0], -x[1]))
        print(cost_list[0][0], cost_list[0][1])