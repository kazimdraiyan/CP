# https://codeforces.com/contest/2146/problem/A
# Status: Accepted

t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split(" ")]

    counts = []
    current_count = 1
    for i in range(1, n):
        if a[i] != a[i-1]:
            counts.append(current_count)
            current_count = 1
        else:
            current_count += 1
    counts.append(current_count)

    counts.sort()
    distinct_numbers = len(counts)
    for i in range(distinct_numbers):
        counts[i] *= (distinct_numbers - i)

    print(max(counts))