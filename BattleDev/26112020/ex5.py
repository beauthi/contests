from itertools import product


def compute_hash(word):
    h = 0
    for i in range(len(word)):
        h += ord(word[i]) * (31 ** (len(word) - i - 1))
    h = h % 4294967296
    return h


chef = input()
chef_hash = compute_hash(chef)

possible_chars = [x for x in range(21, 127)]
size = 2
found = False

minimum_size = 1
current_buffer = chr(126) * minimum_size
while compute_hash(current_buffer) < chef_hash:
    minimum_size += 1
    current_buffer = chr(126) * minimum_size
minimum_size -= 1

maximum_size = len(chef)
current_buffer = chr(21) * maximum_size
while compute_hash(current_buffer) < chef_hash:
    maximum_size += 1
    current_buffer = chr(21) * maximum_size

for size in range(minimum_size, maximum_size):
    for combination in product(possible_chars, repeat=size):
        current_combination = "".join(chr(x) for x in combination)
        if current_combination == chef:
            continue
        current_hash = compute_hash(current_combination)
        if current_hash > chef_hash:
            break
        if current_hash == chef_hash:
            print(current_combination)
            found = True
            break
    if found:
        break
