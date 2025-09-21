# https://codeforces.com/contest/2147/problem/A
# Status: Accepted

t = int(input())
for _ in range(t):
    x, y = [int(v) for v in input().split(" ")]
    if y > x:
        print(2)
    elif x > y + 1 and y != 1:
        print(3)
    else:
        print(-1)
