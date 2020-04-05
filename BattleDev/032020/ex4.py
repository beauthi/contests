from itertools import permutations

def compute_score(sacha_card, my_card):
    if sacha_card == "feu":
        if my_card == "eau":
            return 1
        if my_card == "plante":
            return -1
        if my_card == "glace":
            return -1
        return 0
    if my_card == "feu":
        return - compute_score(my_card, sacha_card)
    if sacha_card == "eau":
        if my_card == "plante":
            return 1
        if my_card == "sol":
            return -1
        return 0
    if my_card == "eau":
        return - compute_score(my_card, sacha_card)
    if sacha_card == "plante":
        if my_card == "poison":
            return -1
        if my_card == "sol":
            return 1
        if my_card == "vol":
            return -1
        return 0
    if my_card == "plante":
        return - compute_score(my_card, sacha_card)
    if sacha_card == "glace" and my_card == "feu":
        return 1
    if sacha_card == "vol" and my_card == "plante":
        return 1
    return 0


n = int(input())
sacha = input().split()
cards = input().split()
perm = permutations(cards)

win = None
for p in perm:
    score =  0
    sacha_card_idx, card_idx = 0, 0
    while sacha_card_idx != len(sacha) and card_idx != len(cards):
        cur_score = compute_score(sacha[sacha_card_idx], p[card_idx])
        if cur_score == 1:
            sacha_card_idx += 1
        elif cur_score == -1:
            card_idx += 1
        else:
            sacha_card_idx +=1
            card_idx += 1
    if sacha_card_idx == len(sacha) and card_idx != len(cards):
        win = p
        break

if win is None:
    print("-1")
else:
    print(" ".join(x for x in win))
