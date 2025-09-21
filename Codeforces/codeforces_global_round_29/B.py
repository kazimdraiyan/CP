# https://codeforces.com/contest/2147/problem/B
# Status: Accepted

t = int(input())

for _ in range(t):
    n = int(input())

    array = [n]
    array.extend(range(n - 1, 0, -1))
    array.append(n)
    array.extend(range(1, n))
    
    print(" ".join(map(str, array)))