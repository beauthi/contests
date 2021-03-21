n, m = tuple(map(int, input().split()))
key = list(map(int, input().split()))
res = list("0" * 256)

prev_xor = [0]
for i in range(0, len(key)):
    prev_xor.append(prev_xor[i] ^ key[i])
for _ in range(m):
    l, r = tuple(map(int, input().split()))
    xor = prev_xor[l] ^ prev_xor[r + 1]
    res[xor] = str(int(res[xor]) + 1)
print(" ".join(res))
