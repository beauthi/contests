class Solution:
    def countAndSay(self, n):
        res, i = "1", 1
        while i < n:
            tmp = ""
            j = 0
            while j < len(res):
                c, count = res[j], 1
                j += 1
                while j < len(res) and res[j] == c:
                    count += 1
                    j += 1
                tmp += str(count) + c
            res = tmp
            i += 1
        return res