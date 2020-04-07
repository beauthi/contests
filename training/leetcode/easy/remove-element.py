class Solution:
    def removeElement(self, nums, val):
        i = 0
        while val in nums:
            nums.remove(val)
        return len(nums)