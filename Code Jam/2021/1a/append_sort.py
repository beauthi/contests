t = int(input())


def determine(a, b):
    i = 0
    min_added = 0
    while i < len(b) and i < len(a) and b[i] == a[i]:
        i += 1
    if len(b) > len(a):
        cur_number = b
    elif i == 0:
        if int(b[i]) < int(a[i]):
            power = len(a) - (len(b) - i) + 1
        elif int(b[i]) > int(a[i]):
            power = len(a) - len(b)
        min_added += power
        cur_number = b + "0" * power
    else:
        if i == len(b) == len(a):
            cur_number = str(int(b) * 10)
            min_added += 1
        elif i == len(b):
            cur_number = str(int(a) + 1)
            min_added += len(a) - i
            if cur_number[:len(b)] != b:
                cur_number = b + "0" * (len(a) - i + 1)
                min_added += 1
        else:
            # TO FIX
            added, nb_str = determine(a[i:], b[i:])
            return min_added + added, a[:i] + nb_str
    return min_added, cur_number


for case in range(t):
    n = int(input())
    digits = input().split()
    min_added = 0
    for d in range(1, n):
        to_add, number = determine(digits[d - 1], digits[d])
        digits[d] = number
        min_added += to_add
    print("Case #{}: {}".format(case + 1, min_added))
