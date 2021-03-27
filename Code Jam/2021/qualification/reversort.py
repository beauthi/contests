n = int(input())
for case in range(n):
    input()
    l = list(map(int, input().split()))
    length = len(l)
    operations = 0
    for i in range(0, length - 1):
        j = l[i:].index(min(l[i:])) + i
        trailing = l[j + 1:] if j != length - 1 else []
        l = l[:i] + list(reversed(l[i:j + 1])) + trailing
        operations += j - i + 1
    print("Case #{}: {}".format(case + 1, operations))