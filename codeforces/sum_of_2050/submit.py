n=int(input())
for _ in range(n):
    cur = int(input())
    if cur % 2050 != 0:
        print("-1")
    else:
        q = 0
        while cur != 0:
            for k in range(18, -1, -1):
                div = 2050 * (10 ** k)
                if cur - div >= 0:
                    cur -= div
                    q += 1
                    break
        print(q)
