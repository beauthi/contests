n = int(input())
for i in range(n):
    x = int(input())
    a, b = x, 0
    idx = str(a).find('4')
    while idx != -1:
        c = int(int(str(a)[idx]) * pow(10, (len(str(a)) - idx - 1)) / 2)
        b += c
        a -= c
        idx = str(a).find('4')

    print("Case #{}: {} {}".format((i + 1), a, b))
