def schedule(intervals):
    result = [None] * len(intervals)
    planning = [0] * 1440
    intervals = enumerate(intervals)
    for i_ivl, interval in sorted(intervals, key=lambda x: x[1][0]):
        subplanning = planning[interval[0]:interval[1]]
        if all(case in [0, 1] for case in subplanning):
            person = 2
        elif all(case in [0, 2] for case in subplanning):
            person = 1
        else:
            return "IMPOSSIBLE"
        for index in range(interval[0], interval[1]):
            planning[index] += person
        result[i_ivl] = "J" if person == 1 else "C"
    return "".join(result)


number_cases = int(input())
for number_case in range(number_cases):
    test_cases = int(input())
    intervals = []
    for test_case in range(test_cases):
        intervals.append(tuple(map(int, input().split())))
    print("Case #{}: {}".format(number_case + 1, schedule(intervals)))
