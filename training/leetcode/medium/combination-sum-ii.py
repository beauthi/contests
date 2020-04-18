class Solution:
    def combinationSum2(self, candidates, target):
        results = []
        for index, candidate in enumerate(candidates):
            c = [candidate]
            if sum(c) == target and c not in results:
                results.append(c)
            elif sum(c) > target:
                continue
            for sub_candidates in self.combinationSum2(candidates[index + 1:], target - sum(c)):
                current_list = c + sub_candidates
                current_list.sort()
                if current_list not in results:
                    results.append(current_list)
        return results

s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))
print(s.combinationSum2([2,5,2,1,2], 5))
print(s.combinationSum2([1, 1], 1))