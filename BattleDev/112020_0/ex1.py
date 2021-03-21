n = int(input())
count = 0
for _ in range(n):
    tn = input()
    if all(x in [str(i) for i in range(10)] for x in tn[-5:]):
        count += 1
print(count)