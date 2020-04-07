class Solution:
    def translate(self, c):
        if c == 'I':
            return 1
        if c == 'V':
            return 5
        if c == 'X':
            return 10
        if c == 'L':
            return 50
        if c == 'C':
            return 100
        if c == 'D':
            return 500
        if c == 'M':
            return 1000

    def romanToInt(self, s):
        res = 0
        i = 0
        count = 0
        while i < len(s):
            c = s[i]
            j = i
            while j < len(s) and c == s[j]:
               count += self.translate(s[j])
               j += 1
            if j < len(s) and count < self.translate(s[j]):
                res -= count
            else:
                res += count
            count = 0
            i = j
        return res