data = list(map(int, input().split()))
ingecables = []
for i in range(data[1]):
    cur = list(map(int, input().split())) + [i + 1]
    ingecables.append(cur)

max_date = max(x[1] for x in ingecables)
dates_cables = []

for y in range(data[0]):
    dates_cables.append(list(0 for x in range(max_date + 1)))

available = True
for date in list(set(x[0] for x in ingecables)):
    current_starting = list(x for x in ingecables if x[0] == date)
    for cur in current_starting:
        for i, line in enumerate(dates_cables):
            available = True
            for place in line[cur[0]:cur[1]]:
                available = available and place == 0
            if available:
                for j in range(cur[0], cur[1]):
                    dates_cables[i][j] = cur[2]
                break
    if not available:
        print("pas possible")
        break
if available:
    results = list(0 for x in range(data[1]))
    for idx, cable in enumerate(dates_cables):
        inges = list(x for x in set(cable) if x != 0)
        for inge in inges:
            results[inge - 1] = idx + 1
    print(" ".join(list(map(str, results))))
