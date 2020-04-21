class Solution:
    def permuteUnique(self, nums: list) -> list:
        if len(nums) == 1:
            return [nums]
        if len(nums) == 2:
            if nums[0] == nums[1]:
                return [[nums[0], nums[1]]]
            return [[nums[0], nums[1]], [nums[1], nums[0]]]
        results = []
        for index, num in enumerate(nums):
            result = [num]
            for other_result in self.permuteUnique(nums[:index] + nums[index + 1:]):
                current_result = result + other_result
                if current_result not in results:
                    results.append(result + other_result)
        return results

s = Solution()
print(s.permuteUnique([1, 1]))
print(s.permuteUnique([1,1,2]))