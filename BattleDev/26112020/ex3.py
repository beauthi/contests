n = int(input())

sons = dict()
for _ in range(n - 1):
    a, b = tuple(map(int, input().split()))
    if b not in sons:
        sons[b] = [a]
    else:
        sons[b] = sons[b] + [a]

index = 0
sizes = [1, len(sons[index]), 0, 0, 0, 0, 0, 0, 0, 0]
level = 1
current_sons = sons[index]
while len(current_sons) > 0:
    tmp_cur_sons = []
    tmp_cur_size = 0
    for current_son in current_sons:
        if current_son in sons:
            tmp_cur_sons.extend(sons[current_son])
        tmp_cur_size += 1
    sizes[level] = tmp_cur_size
    current_sons = tmp_cur_sons
    level += 1

print(" ".join(str(size) for size in sizes))