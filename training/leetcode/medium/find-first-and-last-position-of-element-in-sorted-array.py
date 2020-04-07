class Solution:
    def searchRangeRec(self, nums, target, l, r):
        m = int((r - l) / 2) + l
        if l > r:
            return [-1, -1]
        elif target == nums[m]:
            i = m
            while i >= 0 and nums[i] == target:
                i -= 1
            j = m
            while j < len(nums) and nums[j] == target:
                j += 1
            return [i + 1, j - 1]
        elif target < nums[m]:
            return self.searchRangeRec(nums, target, l, m - 1)
        else:
            return self.searchRangeRec(nums, target, m + 1, r)
    def searchRange(self, nums, target):
        return self.searchRangeRec(nums, target, 0, len(nums) - 1)