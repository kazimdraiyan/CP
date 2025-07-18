# https://vjudge.net/contest/710974#problem/B
# Status: Accepted

def digit_count(num):
    if num < 10:
        return 1
    elif num < 100:
        return 2
    elif num < 1000:
        return 3
    elif num < 10000:
        return 4
    return 5

t = int(input())

for i in range(t):
    stop_number = int(input())
    consisting_digit = stop_number % 10
    n = digit_count(stop_number)
    result = (consisting_digit-1)*10 + n * (n+1) // 2
    print(result)
