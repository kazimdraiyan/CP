# https://vjudge.net/contest/710974#problem/E
# Status: Wrong Answer

import math

def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def slope(p1, p2):
    return (p2[1] - p1[1]) / (p2[0] - p1[0])

t = int(input())

for case_i in range(t):
    nums = input().split(" ")
    points = []
    for i in range(0, 6, 2):
        points.append((int(nums[i]), int(nums[i+1])))
    
    center = points.pop(0)
    r = dist(center, points[0])
    
    m1 = slope(center, points[0])
    m2 = slope(center, points[1])
    
    den = 1 + m1*m2
    if (den == 0):
        angle = math.pi / 2
    else:
        angle = math.atan(abs((m1-m2)/(1+m1*m2)))
    print("Case " + str(case_i+1) + ": " + str(r * angle))
