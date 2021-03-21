def get_possibilities(f):
    possibilities = []
    for i in range(1, (2 ** len(f)) - 1):
        binary = bin(i)[2:]
        possibilities.append("0" * (len(f) - len(binary)) + binary)
    return possibilities


def longest_common_string(f, d):
    possibilities = []
    for possibility in get_possibilities(f):
        included = ""
        f_excluded = ""
        d_excluded = ""
        for index in range(len(possibility)):
            if possibility[index] == '1':
                included += f[index]
            else:
                f_excluded += f[index]
                d_excluded += d[index]
        possibilities.append((included, f_excluded, d_excluded))
        
    return ""
    # possible_str = {}
    # for possibility, _ in f_possibilities:
    #     f_index = 0
    #     d_index = 0
    #     cur_longest_str = ""
    #     while f_index < len(possibility):
    #         if possibility[f_index] not in d[d_index:]:
    #             break
    #         d_index += d[d_index:].index(possibility[f_index]) + 1
    #         cur_longest_str += possibility[f_index]
    #         f_index += 1
    #     if cur_longest_str != "":
    #         if len(cur_longest_str) not in possible_str:
    #             possible_str[len(cur_longest_str)] = []
    #         if cur_longest_str not in possible_str[len(cur_longest_str)]:
    #             possible_str[len(cur_longest_str)].append(cur_longest_str)
    # return possible_str


n = int(input())
articles = []
win = False
for _ in range(n):
    f, d = tuple(input().split())
    s = longest_common_string(f, d)
    if len(s) == 0:
        continue
    for size in sorted(s, reverse=True):
        for p in s[size]:
            prev_d = d
            for c in p:
                d = d.replace(c, "", 1)
            win = not win

if win:
    print("DEBUNK")
else:
    print("FAKE")
