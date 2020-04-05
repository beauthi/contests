n = int(input())

times = []
for _ in range(5):
    times_line = []
    for __ in range(600):
        times_line.append(0)
    times.append(times_line)
for _ in range(n):
    # parse
    line = input().split(' ')
    day = int(line[0])
    if day in [6, 7]:
        continue
    interval = line[1].split('-')
    begin_hour = int(interval[0].split(':')[0])
    begin_minutes = int(interval[0].split(':')[1])
    end_hour = int(interval[1].split(':')[0])
    end_minutes = int(interval[1].split(':')[1])

    # clean input
    if end_hour >= 18:
        end_hour, end_minutes = 17, 59
    if end_hour < 8 or begin_hour >= 18:
        continue
    if begin_hour < 8:
        begin_hour, begin_minutes = 8, 0

    begin_index = (begin_hour - 8) * 60 + begin_minutes
    end_index = (end_hour - 8) * 60 + end_minutes

    for index in range(begin_index, end_index + 1):
        times[day - 1][index] = 1

for day in range(len(times)):
    count = 0
    for minute in range(len(times[day])):
        if times[day][minute] == 0:
            count += 1
        else:
            count = 0
        if count == 60:
            d, m = day, minute - 59
            break
    if count == 60:
        break
d = d + 1
s_h, s_m = int(m / 60) + 8, m % 60
e_h, e_m = int((m + 59) / 60) + 8, (m + 59) % 60
print("{} {}:{}-{}:{}".format(d, s_h, s_m if s_m >= 10 else "0" + str(s_m), e_h, e_m if e_m >= 10 else "0" + str(e_m)))
