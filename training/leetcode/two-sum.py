class Solution:
    def twoSum(self, nums, target):
        for i, elt in enumerate(nums):
            c = target - elt
            if c in nums and nums.index(c) != i:
                return [i, nums.index(c)]