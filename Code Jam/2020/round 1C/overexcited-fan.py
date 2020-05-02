n = int(input())

def solve(positions):
    for index_move, position in enumerate(positions):
        dist = abs(position[0]) + abs(position[1])
        if dist <= index_move:
            return index_move
    return "IMPOSSIBLE"

def position_map(x, y, moves):
    positions = [(x, y)]
    i, j = x, y
    for move in moves:
        if move == "S":
            j = j - 1
        if move == "N":
            j = j + 1
        if move == "E":
            i = i + 1
        if move == "W":
            i = i - 1
        positions.append((i, j))
    return positions

for index in range(n):
    line = list(input().split())
    x, y, moves = int(line[0]), int(line[1]), line[2]
    positions = position_map(x, y, moves)
    result = solve(positions)
    print("Case #{}: {}".format(index + 1, result))
