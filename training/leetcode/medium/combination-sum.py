class Solution:
    def combinationSum(self, candidates, target):
        results = []
        for index, candidate in enumerate(candidates):
            c = [candidate]
            if sum(c) == target:
                results.append(c)
            elif sum(c) > target:
                continue
            for sub_candidates in self.combinationSum(candidates[index:], target - sum(c)):
                results.append(c + sub_candidates)
        return results

s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
print(s.combinationSum([2, 3, 5], 8))
                