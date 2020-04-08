class Solution:
    def firstSolution(self, nums):
        results = []
        for i1 in range(len(nums)):
            for i2 in range(len(nums)):
                if i2 != i1:
                    nums_sum  = nums[i1] + nums[i2]
                    for i3 in range(len(nums)):
                        if (i3 != i1) and (i3 != i2) and ((nums_sum + nums[i3]) == 0):
                            null_sum = sorted((nums[i1], nums[i2], nums[i3]))
                            if null_sum not in results:
                                results.append(null_sum)
        return results

    def secondSolution(self, nums):
        hash_map = {}
        for num in set(nums):
            hash_map[num] = len([x for x in nums if x == num])
        results = []
        for first_value in hash_map:
            for second_value in hash_map:
                for third_value in hash_map:
                    if first_value + second_value + third_value == 0:
                        sorted_values = sorted([first_value, second_value, third_value])
                        if sorted_values not in results:
                            if first_value == second_value == third_value and hash_map[first_value] < 3:
                                continue
                            elif ((first_value == second_value) or (first_value == third_value)) and (hash_map[first_value] < 2):
                                continue
                            elif (third_value == second_value) and (hash_map[third_value] < 2):
                                continue
                            results.append(sorted_values)
        return results
    
    def threeSum(self, nums):
        sorted_nums = sorted(nums)
        results = []
        for i1 in range(len(sorted_nums) - 2):
            if i1 > 0 and sorted_nums[i1] == sorted_nums[i1 - 1]:
                continue
            used = []
            d = set()
            for i2 in range(i1 + 1, len(sorted_nums)):
                if sorted_nums[i2] in used:
                    continue
                if (- sorted_nums[i1] - sorted_nums[i2]) in d:
                    results.append([sorted_nums[i1], - sorted_nums[i1] - sorted_nums[i2], sorted_nums[i2]])
                    used.append(sorted_nums[i2])
                else:
                    d.add(sorted_nums[i2])
        return results

s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([6,-5,-6,-1,-2,8,-1,4,-10,-8,-10,-2,-4,-1,-8,-2,8,9,-5,-2,-8,-9,-3,-5]))
print(s.threeSum([0,0,0]))
print(s.threeSum([-13,10,11,-3,8,11,-4,8,12,-13,5,-6,-4,-2,12,11,7,-7,-3,10,12,13,-3,-2,6,-1,14,7,-13,8,14,-10,-4,10,-6,11,-2,-3,4,-13,0,-14,-3,3,-9,-6,-9,13,-6,3,1,-9,-6,13,-4,-15,-11,-12,7,-9,3,-2,-12,6,-15,-10,2,-2,-6,13,1,9,14,5,-11,-10,14,-5,11,-6,6,-3,-8,-15,-13,-4,7,13,-1,-9,11,-13,-4,-15,9,-4,12,-4,1,-9,-5,9,8,-14,-1,4,14]))
print(s.threeSum([3,-9,3,9,-6,-1,-2,8,6,-7,-14,-15,-7,5,2,-7,-4,2,-12,-7,-1,-2,1,-15,-13,-4,0,-9,-11,7,4,7,13,14,-7,-8,-1,-2,7,-10,-2,1,-10,6,-9,-1,14,2,-13,9,10,-7,-8,-4,-14,-5,-1,1,1,4,-15,13,-12,13,12,-11,12,-12,2,-3,-7,-14,13,-9,7,-11,5,-1,-2,-1,-7,-7,0,-7,-4,1,3,3,9,11,14,10,1,-13,8,-9,13,-2,-6,1,10,-5,-6,0,1,8,4,13,14,9,-2,-15,-13]))