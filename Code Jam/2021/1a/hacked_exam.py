t = int(input())
for case in range(t):
    n, q = tuple(map(int, input().split()))
    best_score = 0
    best_answers = None
    for _ in range(n):
        answers, score = tuple(input().split())
        if best_answers is None:
            best_answers = answers
        if int(score) > best_score:
            best_score = int(score)
            best_answers = answers
    print("Case #{}: {} {}/1".format(case + 1, best_answers, best_score))
