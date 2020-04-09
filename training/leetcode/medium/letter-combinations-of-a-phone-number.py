class Solution:
    def letterCombinations(self, digits: str):
        if len(digits) == 0:
            return []

        mapping = {
            "0": [" "],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        combinations = mapping[digits[0]]
        for char in digits[1:]:
            new_combination = []
            for possible_letter in mapping[char]:
                for combination in combinations:
                    new_combination.append(combination + possible_letter)
            combinations = new_combination
        return combinations

s = Solution()
print(s.letterCombinations("23"))