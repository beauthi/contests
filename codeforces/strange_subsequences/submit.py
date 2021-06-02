def solve(values):
    count = 0
    minimum = max(values) + 2
    for elt in values:
        if elt <= 0:
            count += 1
        else:
            minimum = min(minimum, elt)
    values = sorted(values)
    i = 0
    min_gap = max(values) + 1
    while i + 1 < len(values) and values[i + 1] <= 0:
        min_gap = min(min_gap, values[i + 1] - values[i])
        i += 1
    if min_gap >= minimum:
        return count + 1
    return count


t = int(input())

for case in range(t):
    n = int(input())
    values = list(map(int, input().split()))
    print(solve(values))
