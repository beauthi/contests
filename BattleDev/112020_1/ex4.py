n = int(input())
k = int(input())

courses = 0
cumul = [0]
for _ in range(n):
    current_course = int(input())
    courses += current_course
    cumul.append(current_course + min(cumul[-k-1:]))

# def find_rec(courses):
#     if len(courses) <= k:
#         return sum(courses)
#     sums = []
#     sorted_courses = sorted(courses[:k])
#     median = sorted_courses[int(len(sorted_courses) / 2)]
#     for i in range(1, k + 1):
#         if courses[i] <= median:
#             sums.append(sum(courses[:i]) + find_rec(courses[i + 1:]))
#     return max(sums)


print(courses - min(cumul[-k-1:]))
