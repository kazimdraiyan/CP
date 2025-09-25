import random
from itertools import combinations

m = random.randint(1, 10)
n = random.randint(1, 10)

all = list(range(1, m + 1))

sets = []

for _ in range(n):
    all_copy = all.copy()
    random.shuffle(all_copy)

    to_remove_count = random.randint(0, len(all) - 1)
    for __ in range(to_remove_count):
        all_copy.pop()
    
    sets.append(set(all_copy))

print(n, m)
for set_i in sets:
    l = len(set_i)
    print(l, end=" ")
    for item in set_i:
        print(item, end=" ")
    print()

# inclusion_set_ids = []
for num in range(1, m + 1):
    set_ids_containing_num = []
    for i in range(n):
        if num in sets[i]:
            set_ids_containing_num.append(i)
    print(num, set_ids_containing_num, sep=": ")

way_count = 0
for i in range(1, n + 1):
    combs = combinations(sets, i)
    for comb in combs:
        union = set()
        for set_i in comb:
            union |= set_i
        if union == set(range(1, m + 1)):
            way_count += 1
print(way_count)