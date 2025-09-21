# https://codeforces.com/contest/2126/problem/A
# Status: Accepted

n = int(input())

for i in range(n):
    x = int(input())

    t = x
    while x != 0:
        if t == 0:
            print(t)
            break
        if (x % 10 < t):
            t = x % 10
        x //= 10
    if t != 0:
        print(t)
