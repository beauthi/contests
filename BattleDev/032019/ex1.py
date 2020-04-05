n = int(input())
maps = []
gold = []
mult = []
for i in range(2, n + 2):
    line = input()
    maps.append(line)
    for y, x in enumerate(line):
        if x == 'o':
            gold.append((i - 2, y))
        if x == '*':
            mult.append((i - 2, y))

res = ""
i, j = 0, 0
for x, y in gold:
    if x > i:
        res = res + "v" * abs(x - i)
    else:
        res = res + "^" * abs(x - i)
    if y > j:
        res = res + ">" * abs(y - j)
    else:
        res = res + "<" * abs(y - j)
    res += "x"
    i, j = x, y

for x, y in mult:
    if x > i:
        res = res + "v" * abs(x - i)
    else:
        res = res + "^" * abs(x - i)
    if y > j:
        res = res + ">" * abs(y - j)
    else:
        res = res + "<" * abs(y - j)
    res += "x"
    i, j = x, y

print(res)
