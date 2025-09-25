# https://codeforces.com/contest/2146/problem/B
# Status: On Progress

# Bruteforce

from itertools import combinations

t = int(input())

for _ in range(t):
    n, m = [int(x) for x in input().split()]
    num_set = set(range(1, m + 1))
    way_count = 0

    sets = []
    for i in range(n):
        set_i = {int(x) for x in input().split()[1:]}
        sets.append(set_i)

    # union = set()
    # for set_i in sets:
    #     union |= set_i
    
    # if union != set(range(1, m + 1)):
    #     print("NO")
    # else:
    #     way_count = 1

    # for num in range(1, m + 1):
    #     set_ids_containing_num = []
    #     for i in range(n):
    #         if num in sets[i]:
    #             set_ids_containing_num.append(i)
    #     print(num, set_ids_containing_num, sep=": ")

    for i in range(n, 0, -1):
        combs = combinations(sets, i)
        should_break = False

        for comb in combs:
            union = set()
            for set_i in comb:
                union |= set_i
            if union == num_set:
                way_count += 1
                if way_count == 3:
                    should_break = True
                    break
            elif i == n:
                should_break = True
                break
        
        if should_break:
            break
    
    if way_count >= 3:
        print("YES")
    else:
        print("NO")
