# https://codeforces.com/contest/2126/problem/C
# Status: Accepted

test_case_count = int(input())

for _ in range(test_case_count):
    n, k = [int(x) for x in input().split(" ")] # k = my position
    heights = [int(height) for height in input().split(" ")]
    
    if n == 1:
        print("YES")
        continue
    
    my_height = heights[k-1]

    heights.sort()

    differences = []
    for i in range(n - 1):
        differences.append(heights[i + 1] - heights[i])
    if len(differences) > 0 and my_height < max(differences):
        print("NO")
    else:
        print("YES")
