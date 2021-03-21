n = int(input())
busy = [0] * 60 * (20 - 8)
for _ in range(n):
    begin, end = tuple(input().split("-"))
    b_hour, b_minutes = tuple(map(int, begin.split(":")))
    e_hour, e_minutes = tuple(map(int, end.split(":")))
    b_index = (b_hour - 8) * 60 + b_minutes
    e_index = (e_hour - 8) * 60 + e_minutes
    for index in range(b_index, e_index):
        busy[index] = 1

counter = 0
actual_counter = 0
for busy_minute in busy:
    if busy_minute == 1:
        if counter >= 60:
            actual_counter += counter
        counter = 0
    else:
        counter += 1
if counter >= 60:
    actual_counter += counter
print(actual_counter)
