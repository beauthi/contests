class Solution:
    def search(self, nums: list, target: int) -> int:
        if len(nums) == 0:
            return -1
        if nums[0] > target:
            index = len(nums) - 1
            while index >= 0 and nums[index] > target:
                index -= 1
        else:
            index = 0
            while index <= len(nums) - 1 and nums[index] < target:
                index += 1
        if index == len(nums) or index == - 1 or nums[index] != target:
            return -1
        return index

s = Solution()
print(s.search([4,5,6,7,0,1,2], 0) == 4)
print(s.search([4,5,6,7,0,1,2], 3) == -1)
print(s.search([1], 2) == -1)