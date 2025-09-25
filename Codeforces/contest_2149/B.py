# https://codeforces.com/contest/2149/problem/B
# Status: Accepted

t = int(input())
for _ in range(t):
    n = int(input()) # Even guaranteed
    array = [int(x) for x in input().split()]

    array.sort()

    max_diff = array[1] - array[0]
    for pair_i in range(1, (int)(n / 2)):
        diff = array[pair_i * 2 + 1] - array[pair_i * 2]
        if diff > max_diff:
            max_diff = diff
    
    print(max_diff)
