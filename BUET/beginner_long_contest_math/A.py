# https://vjudge.net/contest/715137#problem/A
# Status: Accepted

import math

t = int(input())

for case in range(1, t+1):
    r1, r2, r3 = [float(num) for num in input().split(" ")]
    
    a = r2 + r3
    b = r3 + r1
    c = r1 + r2

    angle1 = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
    angle2 = math.acos((c ** 2 + a ** 2 - b ** 2) / (2 * c * a))
    angle3 = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))

    a1 = r1 ** 2 * angle1 / 2
    a2 = r2 ** 2 * angle2 / 2
    a3 = r3 ** 2 * angle3 / 2

    triangle_area = math.sqrt((r1 + r2 + r3) * r1 * r2 * r3)

    print(f"Case {case}: {triangle_area - (a1 + a2 + a3)}")
