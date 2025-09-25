import random

n = 100000
k = 90000
arr = []
for _ in range(n):
    arr.append(random.randint(0, n))

with open("cases.txt", "w") as f:
    f.write("1\n")
    f.write(str(n) + " " + str(k) + "\n")
    for elem in arr:
        f.write(str(elem) + " ")
