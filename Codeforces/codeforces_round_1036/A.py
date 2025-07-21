# https://codeforces.com/contest/2124/problem/A
# Status: On Progress

for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split(" ")]

    all_same = True
    for i in range(n-1):
        if a[i] != a[i + 1]:
            all_same = False
            break
    
    if all_same:
        print("NO")