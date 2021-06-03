t = int(input())
for case in range(t):
    k = int(input())
    pgcd = k
    div = 100
    while pgcd > 0 and k % pgcd != 0 or div % pgcd != 0:
        pgcd -= 1
    print(int(div / pgcd))