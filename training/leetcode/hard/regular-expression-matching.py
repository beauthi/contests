class Solution:
    def isMatchRec(self, word: str, tokens: list) -> bool:
        if word == "".join(tokens):
            return True
        if len(word) == 0:
            if all(["*" in x for x in tokens]) or len(tokens) == 0:
                return True
            else:
                return False
        if len(tokens) == 0:
            return False
        current_char = word[0]
        current_token = tokens[0]
        if current_token == current_char:
            return self.isMatchRec(word[1:], tokens[1:])
        else:
            if len(current_token) == 1:
                if current_token == ".":
                    return self.isMatchRec(word[1:], tokens[1:])
                return False
            # current_token is now '.*' or 'a*', 'b*', etc.
            current_token = current_token[0]
            if current_token == ".":
                return self.isMatchRec(word[1:], tokens) \
                    or self.isMatchRec(word, tokens[1:]) \
                    or self.isMatchRec(word[1:], tokens[1:])
            if current_token == current_char:
                return self.isMatchRec(word[1:], tokens) or self.isMatchRec(word, tokens[1:])
            else:
                return self.isMatchRec(word, tokens[1:])

    def isMatch(self, word: str, regex: str) -> bool:
        if word == regex:
            return True
        tokens = []
        index = 0
        while index < len(regex):
            sub_index = index + 1
            while sub_index < len(regex) and regex[sub_index] == "*":
                sub_index += 1
            current_token = regex[index : sub_index]
            if not(len(tokens) > 0 and "*" in current_token and ".*" in tokens[-1]):
                tokens.append(current_token)
            index = sub_index
        return self.isMatchRec(word, tokens)

s = Solution()
print(s.isMatch("aa", "a") == False)
print(s.isMatch("ab", ".*b*") == True)
print(s.isMatch("aab", "c*a*b*") == True)
print(s.isMatch("mississippi", "mis*is*p*.") == False)
print(s.isMatch("celine", "d*a*ce.*l*in.*e") == True)
print(s.isMatch("aaa", "a*a") == True)
print(s.isMatch("fhgiictukvnsfjnvkjfdsnvfdlsvnjkldfsnvjkndfkljsjnvlkdjsnfvkjdfnkvjdfnkjnvfdvoejralkzejjrlkzjklzejrklzjelr", "f.*d.*a*.*") == True)