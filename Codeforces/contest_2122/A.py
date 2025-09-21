# https://codeforces.com/contest/2122/problem/A
# Status: Accepted

for _ in range(int(input())):
    n, m = [int(x) for x in input().split(" ")]

    if n == 1 or m == 1:
        print("NO")
    elif m + n > 4:
        print("YES")
    else:
        print("NO")
