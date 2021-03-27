t = int(input())
lists = []
for case in range(t):
    n, c = tuple(map(int, input().split()))
    if c < (n - 1):
        print("Case #{}: IMPOSSIBLE".format(case + 1))
    else:
        l = list(range(1, n + 1))
        moves = [1] * (n - 1)
        m_index = 0
        right = 0
        while sum(moves) != c and right != len(moves):
            if m_index == len(moves) - right:
                m_index = 0
            if moves[m_index] >= (n - m_index):
                right += 1
                continue
            moves[m_index] += 1
            m_index += 1
        if sum(moves) != c:
            print("Case #{}: IMPOSSIBLE".format(case + 1))
        else:
            index = len(moves) - 1
            while index >= 0:
                move = moves[index]
                l[index:index + move] = list(reversed(l[index:index + move]))
                index -= 1
            print("Case #{}: {}".format(case + 1, " ".join(str(x) for x in l)))
            lists.append(l)
with open("reversort-2.txt", "w") as w:
    w.write(str(len(lists)) + "\n")
    for l in lists:
        w.write(str(len(l)) + "\n")
        w.write(" ".join(str(x) for x in l) + "\n")
