t = int(input())


def mul(l):
    res = 1
    for e in l:
        res *= e
    return res


for case in range(t):
    m = int(input())
    maximum = 0
    deck = []
    for _ in range(m):
        p, n = tuple(map(int, input().split()))
        for __ in range(n):
            deck.append(p)
    for mask in range(pow(2, len(deck))):
        mult = []
        add = []
        mask_bin = bin(mask)[2:]
        for index, digit in enumerate("0" * (len(deck) - len(mask_bin)) + mask_bin):
            if digit == "1":
                mult.append(deck[index])
            else:
                add.append(deck[index])
        s = sum(add)
        if s > maximum and s == mul(mult):
            maximum = s
    print("Case #{}: {}".format(case + 1, maximum))
