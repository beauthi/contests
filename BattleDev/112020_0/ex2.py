n = int(input())

count = 0
found = False
for i in range(n):
    time = input().split(":")
    h = int(time[0])
    m = int(time[1])
    if h >= 20 or h < 8:
        count += 1
    if count > int(n / 2):
        print("SUSPICIOUS")
        found = True
if not found:
    print("OK")