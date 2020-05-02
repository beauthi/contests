t = int(input())
u = int(input())

def solve(inp):
    result = [""] * 10
    for number in range(1, 10):
        if str(number) in inp:
            for possible_number in inp[str(number)]:
                if possible_number not in result:
                    result[number] = possible_number
                    break
    number = 10
    while number < pow(10, 16) and len("".join(result)) < 10:
        if str(number) in inp:
            for possible_number in inp[str(number)]:
                for letter in possible_number:
                    if letter not in result:
                        result[0] = letter
                        return result
        number += 1
    return result

for test_case in range(t):
    inp = dict()
    for _ in range(10000):
        up, rand = tuple(input().split())
        if up in inp:
            inp[up].append(rand)
        else:
            inp[up] = [rand]
    print("Case #{}: {}".format(test_case + 1, "".join(solve(inp))))