from itertools import combinations

n = int(input())

def check_solution(solution):
    moves_x, moves_y = solution
    solution_str = ""
    for power in range(len([x for x in moves_x if x != 0]) + len([y for y in moves_y if y != 0])):
        two = 2 ** power
        if (two not in moves_x and two not in moves_y)\
            and (- two not in moves_x and - two not in moves_y):
            return None
        if two in moves_x:
            solution_str += "E"
        elif - two in moves_x:
            solution_str += "W"
        elif two in moves_y:
            solution_str += "N"
        elif - two in moves_y:
            solution_str += "S"
    return solution_str

def combinationSum(candidates, target):
    results = []
    for length in range(1, len(candidates) + 1):
        for combination in combinations(candidates, length):
            if sum(combination) == target:
                results.append(combination)
    return results

def combi(candidates, target, solution):
    target_x, target_y = target
    if (target_x, target_y) == (0, 0):
        return True, ""
    for index, candidate in enumerate(candidates):
        succ, sol = combi(candidates[index + 1:], (target_x - candidate, target_y), solution)
        if succ:
            return True, solution + "W"
        succ, sol = combi(candidates[index + 1:], (target_x + candidate, target_y), solution)
        if succ:
            return True, solution + "E"
        succ, sol = combi(candidates[index + 1:], (target_x, target_y - candidate), solution)
        if succ:
            return True, solution + "S"
        succ, sol = combi(candidates[index + 1:], (target_x, target_y + candidate), solution)
        if succ:
            return True, solution + "N"
    return False, ""

def find_solutions(goal_x, goal_y, powers):
    solution = ""
    combi(powers, (goal_x, goal_y), solution)
    return solution
    powers += [-x for x in powers]
    possible_values_x = combinationSum(powers, goal_x)
    possible_values_y = combinationSum(powers, goal_y)
    if goal_x == 0:
        possible_values_x.append([0])
    if goal_y == 0:
        possible_values_y.append([0])
    possible_values_x.sort(key=lambda x : len(x))
    possible_values_y.sort(key=lambda x : len(x))

    solutions = []
    for possible_value_x in possible_values_x:
        for possible_value_y in possible_values_y:
            good = True
            for x in possible_value_x:
                if abs(x) in [abs(elt) for elt in possible_value_y]:
                    good = False
                    break
            if good:
                possible = check_solution((possible_value_x, possible_value_y))
                if possible is not None:
                    return possible
    if len(solutions) == 0:
        return "IMPOSSIBLE"
    return solutions

for case in range(n):
    goal_x, goal_y = tuple(map(int, input().split()))
    powers = []
    p, power = 0, 1
    while power <= abs(goal_x) + abs(goal_y):
        powers.append(power)
        p += 1
        power = 2 ** p
    solution = find_solutions(goal_x, goal_y, powers)
    print("Case #{}: {}".format(case + 1, solution))
