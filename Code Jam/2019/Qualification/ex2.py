n = int(input())
for i in range(n):
    dimensions = int(input())
    path = input()
    trans = {
        'S' : 'E',
        'E' : 'S'
    }
    res = "".join([trans[x] for x in path])
    print("Case #{}: {}".format((i + 1), res))
