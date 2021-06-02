nb_cases = int(input())

for case in range(nb_cases):
    a, b = tuple(map(int, input().split()))
    n = int(input())
    answer = ""
    mid = 0
    while answer != "CORRECT" and n != 0:
        if answer == "TOO_BIG":
            n = mid - 1
        if answer == "TOO_SMALL":
            a = mid + 1
        mid = int((a + n) / 2)
        print(mid, flush=True)
        answer = input()
        n -= 1
