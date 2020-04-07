class Solution:
    def longestCommonPrefix(self, strs):
        if not len(strs):
            return ""
        res = ""
        for i in range(min(map(len, strs))):
            c = strs[0][i]
            for word in strs:
                if word[i] != c:
                    return res
            res = res + c
        return res