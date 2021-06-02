from itertools import permutations

H = pow(10, 9) * 3600
M = pow(10, 9) * 60
S = pow(10, 9)
D = 12 * pow(10, 10)  # tick in degrees

t = int(input())
for case in range(t):
    a, b, c = tuple(map(int, input().split()))
    found = False
    for rotation in range(0, 360):
        ticks = rotation * D
        for x, y, z in permutations([(a + ticks) % (360 * D), (b + ticks) % (360 * D), (c + ticks) % (360 * D)]):
            if found:
                break
            h, m, s = x, int(y / 12), int(z / 720)
            print(m, h % H)
            if m == h % H and s == (h % H) % M:
                print("Case #{}: {} {} {} {}".format(case + 1, int(h / H), int((h % H) / M), int(((h % H) % M) / S), ((h % H) % M) % S))
                found = True
    exit()