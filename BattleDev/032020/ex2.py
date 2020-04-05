n = int(input())
prev = None
length = 0
for _ in range(n):
    x = int(input())
    if prev is None:
        cur_length = 1
    else:
        if x == prev:
            cur_length += 1
            if cur_length > length:
                length = cur_length
        else:
            if cur_length > length:
                length = cur_length
            cur_length = 1
    prev = x
    if cur_length > length:
        length = cur_length
print(length)
