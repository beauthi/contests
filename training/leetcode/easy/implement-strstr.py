class Solution:
    def strStr(self, haystack, needle):
        return 0 if needle == "" else -1 if needle not in haystack else haystack.index(needle)