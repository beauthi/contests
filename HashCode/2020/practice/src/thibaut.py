inp = input().split()
m,n = int(inp[0]), int(inp[1])
pizzas = list(map(int, input().split()))

soluce = []
for i in range(n - 1, 0, -1):
    soluce.append(i)
    if sum(pizzas[x] for x in soluce) > m:
        soluce.pop()
    if sum(pizzas[x] for x in soluce) == m:
        break
for i in range(n):
    if i not in soluce:
        soluce.append(i)
    if sum(pizzas[x] for x in soluce) > m:
        soluce.pop()
        break
    if sum(pizzas[x] for x in soluce) == m:
        break
print(len(soluce))
print(" ".join(str(x) for x in soluce))