n = int(input())
a = list(map(int, input().split()))
s = sum(a)

if s != 0:
    print("YES")
    print("1")
    print("1 {}".format(n))
else:
    i = 0
    while i < n and a[i] == 0:
        i += 1
    if i == n:
        print("NO")
    else:
        print("YES")
        print("2")
        print("{} {}".format(1, i + 1))
        print("{} {}".format(i + 2, n))