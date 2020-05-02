t = int(input())

def solve(angles, d):
    angles_dict = dict()
    for angle in angles:
        if angle in angles_dict:
            angles_dict[angle] += 1
            if angles_dict[angle] == d:
                return 0
        else:
            angles_dict[angle] = 1
    angles_sorted = sorted(angles_dict.keys())
    for index, angle in enumerate(angles_sorted):
        if angles_dict[angle] > 1 and (sum(a * angles_dict[a] for a in angles_sorted[index + 1:]) / (d - angles_dict[angle])) >= angle:
            return angle
    mini = d - 1
    for index, angle in enumerate(angles_sorted):
        count = 0
        slices = 1
        for other_angle in angles_sorted[index + 1:]:
            slices_more = int(other_angle / angle)
            if other_angle % angle == 0:
                count += slices_more - 1
            else:
                count += slices_more
            slices += slices_more
            diff = slices - d
            if diff >= angle * 2:
                count = count - (int(diff / angle) - 1)
            #print(angle, other_angle, slices_more, count, slices, diff)
            if count < mini and slices >= d:
                mini = count
                break
    return int(mini)

for case in range(t):
    _, d = tuple(map(int, input().split()))
    angles = tuple(map(int, input().split()))
    print("Case #{}: {}".format(case + 1, solve(angles, d)))
