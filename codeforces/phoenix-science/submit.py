t = int(input())
for case in range(t):
    n = int(input())
    i = 1
    l = [1]
    while sum(l) <= n:
        i *= 2
        l.append(i)
    if sum(l) > n:
        l.pop()
    if sum(l) != n:
        l.append(n - sum(l))
    l = sorted(l)
    print(len(l) - 1)
    for i in range(len(l) - 1):
        print(l[i + 1] - l[i], end=" ")
    print()