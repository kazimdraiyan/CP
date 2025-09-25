from itertools import combinations

iter = range(0, 30)
combs = combinations(iter, 10)

i = 0
for comb in combs:
    print(comb)
    i += 1
    if i == 3:
        break

print(combs)
