class Solution:
    def getAnagram(self, word : str) -> bool:
        word_letters = {}
        for letter in word:
            if letter in word_letters:
                word_letters[letter] += 1
            else:
                word_letters[letter] = 1
        return word_letters
    def groupAnagrams(self, strs: list) -> list:
        results = []
        for word in strs:
            found = False
            current_anagram = self.getAnagram(word)
            for group in results:
                if current_anagram == group['anagram']:
                    group['list'].append(word)
                    found = True
                    break
            if not found:
                results.append({
                    'anagram' : current_anagram,
                    'list' : [word]
                })
        return [l['list'] for l in results]

s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))