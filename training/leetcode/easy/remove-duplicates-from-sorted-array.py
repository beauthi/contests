class Solution:
    def removeDuplicates(self, nums):
        i = 0
        tmp = []
        while i < len(nums):
            if nums[i] not in tmp:
                tmp.append(nums[i])
            i += 1
        while len(nums) > 0:
            nums.remove(nums[0])
        for elt in tmp:
            nums.append(elt)