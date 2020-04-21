class Solution:
    def permute(self, nums: list) -> list:
        if len(nums) == 1:
            return [nums]
        if len(nums) == 2:
            return [[nums[0], nums[1]], [nums[1], nums[0]]]
        results = []
        for index, num in enumerate(nums):
            result = [num]
            for other_result in self.permute(nums[:index] + nums[index + 1:]):
                results.append(result + other_result)
        return results

s = Solution()
print(s.permute([]))
print(s.permute([1]))
print(s.permute([1, 2]))
print(s.permute([1, 2, 3]))
print(s.permute([1, 2, 3, 4]))