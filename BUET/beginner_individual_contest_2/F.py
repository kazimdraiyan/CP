# https://vjudge.net/contest/710974#problem/F
# Status: Accepted

q = int(input())

def index_in_region(k, region_num):
    if (k % region_num == 0):
        return k // region_num
    return k // region_num + 1

for _ in range(q):
    k = int(input())

    region_num = 1
    while (k - 9 * 10 ** (region_num-1) * region_num > 0):
        k -= 9 * 10 ** (region_num-1) * region_num
        region_num += 1

    n = index_in_region(k, region_num)
    number = 10 ** (region_num - 1) + n - 1
    index_in_number = k % region_num - 1
    print(str(number)[index_in_number])
