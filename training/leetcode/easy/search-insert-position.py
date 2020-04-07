class Solution:
    def searchInsert(self, nums, target):
        i = 0
        while i < len(nums) and nums[i] < target:
            i += 1
        return i