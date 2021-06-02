def answer(q):
    sorted_list = []
    slots = list(reversed(list([x, x + 1, x + 2] for x in range(1, n - 1))))
    while q != 0 and len(slots) > 0:
        slot = slots.pop()
        print(" ".join(str(x) for x in slot), flush=True)
        median = int(input())
        with open("output.txt", "a+") as w:
            w.write(str(median) + "\n")
        slot.remove(median)
        if slot[0] in sorted_list:
            x0 = sorted_list.index(slot[0])
        else:
            x0 = -1
        if slot[1] in sorted_list:
            x1 = sorted_list.index(slot[1])
        else:
            x1 = -1
        if median in sorted_list:
            m = sorted_list.index(median)
        else:
            m = -1
        if x0 == -1 and x1 == -1:
            sorted_list = [slot[0], median, slot[1]]
        else:
            if m == -1:
                if abs(x0 - x1) == 1:
                    sorted_list.insert(max(x0, x1), median)
                else:
                    t_list = sorted_list[:]
                    t_list.insert(min(x0, x1) + 1, median)
                    for i in range(min(x0, x1), max(x0, x1) - 1):
                        slots.append([t_list[i], t_list[i + 1], t_list[i + 2]])
            if x0 == -1:
                if m > x1:
                    sorted_list.insert(m + 1, slot[0])
                else:
                    if m == 0:
                        sorted_list.insert(0, slot[0])
                    else:
                        sorted_list.insert(m - 1, slot[0])
            if x1 == -1:
                if m > x0:
                    sorted_list.insert(m + 1, slot[1])
                else:
                    if m == 0:
                        sorted_list.insert(0, slot[1])
                    else:
                        sorted_list.insert(m - 1, slot[1])
        q -= 1
    print(" ".join(str(x) for x in sorted_list), flush=True)
    if input() == "-1":
        return -1
    else:
        return q


t, n, q = tuple(map(int, input().split()))
q_left = q
for _ in range(n):
    q_left = answer(q_left)
    if q_left == -1:
        break
