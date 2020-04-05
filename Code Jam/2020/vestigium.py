def trace(matrix):
    result = 0
    for i, row in enumerate(matrix):
        result += row[i]
    return result

def rep_rows(matrix):
    result = 0
    for row in matrix:
        if len(set(row)) != len(row):
            result += 1
    return result

def rep_col(matrix):
    result = 0
    for col in range(len(matrix)):
        column = []
        for row in matrix:
            column.append(row[col])
        if (len(set(column))) != len(column):
            result += 1
    return result

number_tests = int(input())
for test in range(number_tests):
    size = int(input())
    matrix = []
    for row in range(size):
        matrix.append(list(map(int, input().split())))
    t = trace(matrix)
    r = rep_rows(matrix)
    c = rep_col(matrix)
    print("Case #{}: {} {} {}".format(test + 1, t, r, c))
