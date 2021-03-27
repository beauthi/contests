n = int(input())
for case in range(1, n + 1):
    line = input().split()
    prices = {}
    prices['CJ'] = int(line[0])
    prices['JC'] = int(line[1])
    s = line[2]
    index = 0
    tokens = []
    # tokenizer
    while index < len(s) - 1:
        sub_index = index + 1
        cur_letter = s[index]
        while sub_index < len(s) and s[sub_index] in [cur_letter, '?']:
            sub_index += 1
        tokens.append(s[index:sub_index + 1])
        index = sub_index
    cost = 0
    for token in tokens:
        if len(token) == 2:
            if token in prices:
                cost += prices[token]
        else:
            left, right = token[0], token[-1]
            if left != right and left != '?' and right != '?':
                cost += prices[left + right]
    print("Case #{}: {}".format(case, cost))
