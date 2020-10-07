class Solution:
    def jump(self, nums: list) -> int:
        count = 0
        index = 0
        while index < len(nums) - 1:
            m = index, 0
            for sub_index, jump in enumerate(nums[index + 1 : index + 1 + nums[index]]):
                if (index + 1 + sub_index) == (len(nums) - 1):
                    return count + 1
                preview_index = index + 1 + sub_index + jump
                if preview_index > m[1]:
                    m = index + 1 + sub_index, preview_index
            index = m[0]
            count += 1
        return count

s = Solution()
print(s.jump([2,3,1,1,4]) == 2)
print(s.jump([3,2,1]) == 1)