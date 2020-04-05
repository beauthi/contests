n = int(input())
words = []
for x in range(2, n + 2):
    words.append(input())

common = []
for letter in words[0]:
    if all(letter in w for w in words) and letter not in common:
        m = len(words[0])
        for w in words:
            cur = len(list(x for x in w if x == letter))
            if cur < m:
                m = cur
        for i in range(m):
            common.append(letter)

if len(common) == 0:
    print("KO")

from itertools import permutations
import re

for x in range(len(common), 0, -1):
    perms = list(permutations(common, x + 1))
    for perm in perms:
        patt = ".*" + ".*".join(perm) + ".*"
        pattern = re.compile(patt)
        if all(pattern.match(w) is not None for w in words):
            print("".join(perm))
            exit()
print("KO")
