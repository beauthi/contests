import sys


def compute_jamal(prices, s):
    index = 0
    tokens = []
    # tokenizer
    while index < len(s) - 1:
        sub_index = index + 1
        cur_letter = s[index]
        while sub_index < len(s) and s[sub_index] != "?" and s[sub_index] == cur_letter:
            sub_index += 1
        if sub_index == index + 1:
            while sub_index < len(s) and s[sub_index] in [cur_letter, '?']:
                sub_index += 1
        else:
            sub_index -= 1
        tokens.append(s[index:sub_index + 1])
        index = sub_index
    cost = 0
    for token in tokens:
        if not any(x == "?" for x in token):
            for index in range(0, len(token) - 1):
                cur_token = token[index] + token[index + 1]
                cost += prices[cur_token]
        else:
            left, right = token[0], token[-1]
            i_beg, i_end = 0 if left == "?" else 1, len(token) if right == "?" else len(token) - 1
            cj, jc = "", ""
            for i in range(i_beg, i_end):
                cj += "J" if i % 2 == 1 else "C"
                jc += "C" if i % 2 == 1 else "J"
            payloads = set(["J" * (i_end - i_beg), "C" * (i_end - i_beg), cj, jc])
            left_pl = "" if left == "?" else left
            right_pl = "" if right == "?" else right
            best_cost = sys.maxsize
            for payload in payloads:
                full_pl = left_pl + payload + right_pl
                cur_cost = compute_jamal(prices, full_pl)
                if cur_cost < best_cost:
                    best_cost = cur_cost
            cost += best_cost
    return cost


#print(compute_jamal({'CJ': 2, 'JC': -2, 'JJ': 0, 'CC': 0}, sys.argv[1]))
#exit()
n = int(input())
for case in range(1, n + 1):
    line = input().split()
    prices = {}
    prices['CJ'] = int(line[0])
    prices['JC'] = int(line[1])
    prices['JJ'] = 0
    prices['CC'] = 0
    s = line[2]
    cost = compute_jamal(prices, s)
    print("Case #{}: {}".format(case, cost))
