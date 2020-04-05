beats = {
    'R': 'S',
    'S': 'P',
    'P': 'R'
}

t = int(input())
for i in range(t):
    a = int(input())
    adversaries = list()
    for j in range(a):
        adversaries.append(input())

    adversaries = list(set(adversaries))
    res = ""
    x = 0
    while len(adversaries) != 0:
        current_letters = set([adv[x % len(adv)] for adv in adversaries])
        chosen = None
        for letter in ["R", "S", "P"]:
            if not any(beats[c] == letter for c in current_letters):
                if chosen is None:
                    chosen = letter
                elif any(beats[letter] == c for c in current_letters):
                    chosen = letter
        if chosen is not None:
            res += chosen
            adversaries_new = []
            for adv in adversaries:
                if adv[x % len(adv)] != beats[chosen]:
                    adversaries_new.append(adv)
            adversaries = adversaries_new
            if len(adversaries) == 0:
                break
        else:
            res = "IMPOSSIBLE"
            break
        x += 1
    print("Case #{}: {}".format(i + 1, res))
