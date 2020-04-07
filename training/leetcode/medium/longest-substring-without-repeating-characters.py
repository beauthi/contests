class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        cur = 0
        i = 1
        maxi = 1
        while i < len(s):
            if s[i] in s[cur:i]:
                maxi = max(i - cur, maxi)
                cur = i - s[i-1::-1].index(s[i])
            i += 1
        maxi = max(i - cur, maxi)
        return maxi