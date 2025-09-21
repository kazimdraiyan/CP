# https://codeforces.com/contest/2122/problem/B
# Status: On Progress

class Pile:
    num_of_zeros: int = 0
    num_of_ones: int = 0
    target_num_of_zeros: int = 0
    target_num_of_ones: int = 0

    def __init__(self, num_of_zeros: int, num_of_ones: int, target_num_of_zeros: int, target_num_of_ones: int):
        self.num_of_zeros = num_of_zeros
        self.num_of_ones = num_of_ones
        self.target_num_of_zeros = target_num_of_zeros
        self.target_num_of_ones = target_num_of_ones
    
    # +ve: needs zeros, -ve: has extra zeros
    def del_zeros(self) -> int:
        return self.target_num_of_zeros - self.num_of_zeros

    # +ve: needs ones, -ve: has extra ones
    def del_ones(self) -> int:
        return self.target_num_of_ones - self.num_of_ones

    def target_completed(self) -> bool:
        return self.del_zeros() == 0 and self.del_ones() == 0

    def __str__(self) -> str:
        # return "0\n" * self.num_of_zeros + "1\n" * self.num_of_ones + "TO\n" + "0\n" * self.target_num_of_zeros + "1\n" * self.target_num_of_ones
        return f"ZERO: {self.num_of_zeros} -> {self.target_num_of_zeros} | ONE: {self.num_of_ones} -> {self.target_num_of_ones}"

    def __repr__(self):
        return str(self)


for _ in range(int(input())):
    n = int(input())

    piles: list[Pile] = []
    steps = 0

    for i in range(n):
        pile = Pile(*(int(x) for x in input().split(" ")))
        if (pile.num_of_zeros != pile.target_num_of_zeros or pile.num_of_ones != pile.target_num_of_ones): # If already satisfied, don't add
            piles.append(pile)
    
    print(piles)
    for i in range(len(piles)):
        for j in range(len(piles)):
            if piles[i].del_zeros() < 0: # Has extra zeros
                if i == j or piles[j].del_zeros() <= 0 or piles[j].del_ones() < 0:
                    continue
                # Pile 2 needs zeros, and do not have extra ones
                transfer = min(-piles[i].del_zeros(), piles[j].del_zeros())
                piles[i].num_of_zeros-= transfer
                piles[j].num_of_zeros += transfer
                steps += transfer
        print(piles)