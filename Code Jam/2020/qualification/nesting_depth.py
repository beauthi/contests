# contains no "0"
def nested(s):
    if len(s) == 0:
        return ""
    s = s + "0"
    prev = int(s[0])
    result = prev * '(' + str(prev)
    index = 1
    while index < len(s):
        number = int(s[index])
        difference = number - prev
        if difference > 0:
            result = result + '(' * abs(difference) + str(number)
        elif difference < 0:
            result = result + ')' * abs(difference) + str(number)
        else:
            result = result + str(number)
        prev = number
        index += 1

    return result[:-1]

number_examples = int(input())
for example in range(number_examples):
    s = input()
    print("Case #{}: {}".format(example + 1, nested(s)))
