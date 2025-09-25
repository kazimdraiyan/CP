import random

n = 100000

with open("cases.txt", "w") as f:
    f.write("1\n")
    f.write(str(n) + "\n")
    for _ in range(n):
        if random.randint(0, 1) == 0:
            f.write("a")
        else:
            f.write("b")
