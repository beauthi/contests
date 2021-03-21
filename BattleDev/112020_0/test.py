mem = dict()


def get_all_children_string(s):
    """
        gets all 2-partitions of the string s
    """
    children = set()
    for bitmask in range(2**len(s)-1):
        taken, left = [], []
        b = 1
        for i in range(len(s)):
            if (b & bitmask) == 0:
                left += [s[i]]
            else:
                taken += [s[i]]
            b *= 2
        children.add(("".join(taken), "".join(left)))
    return children


def get_all_children_pair(f, d):
    """
        gets all pairs of strings that we can get from the pair (f,d)
    """
    children_f, children_d = get_all_children_string(f), get_all_children_string(d)
    res = set()
    for taken_f, left_f in children_f:
        for taken_d, left_d in children_d:
            if left_f == left_d:
                res.add((taken_f, taken_d))
    return res


def get_mex(f, d):
    """
        computes the Minimum EXcluded for a given state
    """
    if (f, d) not in mem:
        excluded = set()
        children = get_all_children_pair(f, d)
        for new_f, new_d in children:
            excluded.add(get_mex(new_f, new_d))
        res = 0
        while res in excluded:
            res += 1
        mem[(f, d)] = res
    return mem[(f, d)]


print(get_mex("cabb", "abbd"))
