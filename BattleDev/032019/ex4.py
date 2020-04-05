data = list(map(int, input().split()))
n = data[0]
m = data[1]
c = data[2]

pierres = []
for i in range(n):
    pierres.append(list(map(int, input().split())))
poudres = []
for i in range(m):
    poudres.append(list(map(int, input().split())))

ratio_pierres = list([x[0]/x[1], x[1], 1] for x in pierres)
ratio_poudres = list([x[0]/1, x[1], 2] for x in poudres)
ratios = list(x for x in enumerate(ratio_pierres + ratio_poudres))

g_left = c
fortune = 0

while g_left != 0:
    started_gleft = g_left
    sorted_ratios = sorted(ratios, key=lambda x: x[1][0], reverse=True)
    best_ones = list(x for x in sorted_ratios if x[1][0] == max(x_[1][0] for x_ in ratios))
    for i, best_one in best_ones:
        if best_one[2] == 1: # pierre
            if best_one[1] <= g_left:
                g_left = g_left - best_one[1]
                fortune = fortune + best_one[0] * best_one[1]
                ratios[i][1][1] -= best_one[1]
        if best_one[2] == 2: # poudre
            grams_optimal = min(best_one[1], g_left)
            g_left = g_left - grams_optimal
            fortune = fortune + best_one[0] * grams_optimal
            ratios[i][1][1] -= grams_optimal
    new_ratios = []
    for ratio in ratios:
        if not(ratio[1][1] == 0 or (ratio[1][2] == 1 and ratio[1][1] > g_left)):
            new_ratios.append([len(new_ratios), ratio[1]])
    ratios = new_ratios[:]
    if started_gleft == g_left:
        break
print(int(fortune))
