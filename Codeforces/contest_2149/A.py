# https://codeforces.com/contest/2149/problem/A
# Status: Accepted

t = int(input())
for _ in range(t):
    n = int((input()))
    array = [int(x) for x in input().split()]

    count = 0
    if (array.count(-1) % 2 == 1):
        count += 2
    
    count += array.count(0)

    print(count)
