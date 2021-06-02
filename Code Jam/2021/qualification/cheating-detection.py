Q = 10000
N = 100
t = int(input())
p = int(input())
for case in range(t):
    players = []
    for _ in range(N):
        players.append(list(map(int, input())))
    average = [None] * Q
    for q in range(Q):
        average[q] = round(sum(player[q] for player in players) / Q)
    n_different = [0] * N
    for n, player in enumerate(players):
        for q in range(Q):
            if average[q] != player[q]:
                n_different[n] += 1
    print("Case #{}: {}".format(case + 1, n_different.index(max(n_different)) + 1))