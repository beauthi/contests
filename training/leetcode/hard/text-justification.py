class Solution:
    def fullJustify(self, words, maxWidth):
        index = 0
        wordsLength = len(words)
        lines = []
        while index < wordsLength:
            tmp_index = index
            for numberOfWords in range(1, wordsLength - index + 1):
                tmp_words = words[index : index + numberOfWords]
                tmp_length = len(tmp_words) - 1 + sum(len(word) for word in tmp_words)
                if tmp_length <= maxWidth:
                    currentWords = tmp_words
                    tmp_index += 1
                else:
                    break
            if len(currentWords) == 1:
                currentWords += " " * (maxWidth - len(currentWords[0]))
            else:
                if tmp_index == wordsLength:
                    currentWords = " ".join(currentWords)
                    currentWords += " " * (maxWidth - sum(len(word) for word in currentWords))
                else:
                    spaces = [" " for word in currentWords[:-1]]
                    index_spaces = 0
                    while sum(len(word) for word in currentWords) + sum(len(x) for x in spaces) != maxWidth:
                        spaces[index_spaces] += " "
                        index_spaces = (index_spaces + 1) % len(spaces)
                    for i in range(len(currentWords) - 1):
                        currentWords[i] += spaces[i]
            currentWords = "".join(currentWords)
            lines += [currentWords]
            index = tmp_index
        return lines

s = Solution()
print(s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
print(s.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))