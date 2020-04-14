class Solution:
    def firstSolution(self, nums):
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[j], nums[i] = nums[i], nums[j]
        else:
            nums[:] = nums[::-1]
    def nextPermutation(self, nums):
        i = len(nums) - 1
        while i >= 1 and nums[i] <= nums[i - 1]:
            i -= 1
        if i > 0:
            j = i
            next_larger = j
            while j < len(nums):
                if nums[j] > nums[i - 1] and nums[j] <= nums[next_larger]:
                    next_larger = j
                j += 1
            nums[next_larger], nums[i - 1] = nums[i - 1], nums[next_larger]
            nums[i:] = nums[i::][::-1]
        else:
            nums[:] = nums[::-1]

s = Solution()
nums = [1, 2, 3]
s.nextPermutation(nums)
print(nums == [1, 3, 2])
nums = [3, 2, 1]
s.nextPermutation(nums)
print(nums == [1, 2, 3])
nums = [1, 1, 5]
s.nextPermutation(nums)
print(nums == [1, 5, 1])
nums = [1, 3, 2]
s.nextPermutation(nums)
print(nums == [2, 1, 3])
nums = [2, 3, 1, 3, 3]
s.nextPermutation(nums)
print(nums)
print(nums == [2, 3, 3, 1, 3])