def common_divisor(a, b):
    for x in range(2, a + 1):
        if a % x == 0 and b % x == 0:
            return True
    return False

n = int(input())
a = int(n / 2)
b = n - a
while a % b == 0 or common_divisor(a, b):
    a, b = a - 1, b + 1
print(a, b)