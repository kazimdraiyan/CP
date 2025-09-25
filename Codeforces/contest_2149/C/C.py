# https://codeforces.com/contest/2149/problem/C
# Status: Accepted

t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    array = [int(x) for x in input().split()]

    smaller_nums = set(range(k))
    intersect = set(array) & smaller_nums
    
    print(max(k - len(intersect), array.count(k)))
