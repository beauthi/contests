#! /usr/bin/python3

n = int(input())
for case in range(n):
    p, q = tuple(map(int, input().split()))
    grid = [[0] * (q + 1) for _ in range(q + 1)]
    for _ in range(p):
        x, y, d  = tuple(input().split())
        x, y = int(x), int(y)
        if d == "N":
            for i in range(q + 1):
                for j in range(y + 1, q + 1):
                    grid[i][j] += 1
        elif d == "S":
            for i in range(q + 1):
                for j in range(y - 1, -1, -1):
                    grid[i][j] += 1
        elif d == "W":
            for j in range(q + 1):
                for i in range(x - 1, -1, -1):
                    grid[i][j] += 1
        elif d == "E":
            for j in range(q + 1):
                for i in range(x + 1, q + 1):
                    grid[i][j] += 1
    position = (q + 1, q + 1)
    maximum = -1
    for i, l in enumerate(grid):
        for j, elt in enumerate(l):
            if elt > maximum:
                position = (i, j)
                maximum = elt
            elif elt == maximum:
                if i < position[0]:
                    position = (i, j)
                elif i == position[0] and j < position[1]:
                    position = (i, j)
    print("Case #{}: {} {}".format(case + 1, position[0], position[1]))
