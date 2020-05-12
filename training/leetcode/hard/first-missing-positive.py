class Solution:
    def firstMissingPositive(self, nums : list) -> int:
        nums = sorted(set([x for x in nums if x > 0]))
        if len(nums) == 0 or nums[0] - 1 > 0:
            return 1
        index = 1
        while index < len(nums):
            if nums[index] != (nums[index - 1] + 1):
                return nums[index - 1] + 1
            index += 1
        return nums[-1] + 1

s = Solution()
print(s.firstMissingPositive([1,2,0]) == 3)
print(s.firstMissingPositive([3,4,-1,1]) == 2)
print(s.firstMissingPositive([7,8,9,11,12]) == 1)
print(s.firstMissingPositive([]) == 1)
print(s.firstMissingPositive([0,2,2,1,1]) == 3)