class Solution:
    def firstSolution(self, s: str, p: str) -> bool:
        if s == p or p == "*":
            return True
        if p == "":
            return False
        if s == "":
            if p[0] == "*":
                return self.isMatchRec(s, p[1:])
            else:
                return False
        if p[0] == "?":
            return self.isMatchRec(s[1:], p[1:])
        if p[0] == "*":
            return self.isMatchRec(s[1:], p[1:]) or self.isMatchRec(s, p[1:]) or self.isMatchRec(s[1:], p)
        if p[0] == s[0]:
            return self.isMatchRec(s[1:], p[1:])
        return False
    def isMatch(self, s: str, p: str) -> bool:
        index = 0
        p_list = []
        acc = ""
        while index < len(p):
            if p[index] != "*":
                acc += p[index]
            else:
                if acc != "":
                    p_list.append(acc)
                    acc = ""
                if len(p_list) == 0 or (len(p_list) > 0 and p_list[-1] != "*"):
                    p_list.append("*")
            index += 1
        if acc != "":
            p_list.append(acc)

        index = 0
        s_index = 0
        while index < len(p_list):
            token = p_list[index]
            if token == "*":
                if index + 1 < len(p_list):
                    next_token = p_list[index + 1]
                    if index + 2 == len(p_list):
                        if len(next_token) > len(s[s_index:]):
                            return False
                        for i, c in enumerate(next_token):
                            if c != '?' and c != s[len(s) - len(next_token) + i]:
                                return False
                        return True
                    next_token_index = s_index
                    while next_token_index < len(s):
                        next_token_index_bis = 0
                        while (next_token_index + next_token_index_bis) < len(s) and next_token_index_bis < len(next_token):
                            if next_token[next_token_index_bis] != '?' and s[next_token_index + next_token_index_bis] != next_token[next_token_index_bis]:
                                break
                            next_token_index_bis += 1
                        if next_token_index_bis == len(next_token):
                            break
                        next_token_index += 1
                    if next_token_index == len(s):
                        return False
                    index += 2
                    s_index = next_token_index + next_token_index_bis
                else:
                    return True
            else:
                for i, c in enumerate(token):
                    if s_index + i == len(s):
                        return False
                    if c != '?' and c != s[s_index + i]:
                        return False
                s_index += len(token)
                index += 1
        return s_index == len(s)

s = Solution()
print(s.isMatch("abefcdgiescdfimde", "ab*cd?i*de") == True)
print(s.isMatch("aa", "a") == False)
print(s.isMatch("a", "aa") == False)
print(s.isMatch("aa", "*") == True)
print(s.isMatch("cb", "?a") == False)
print(s.isMatch("adceb", "*a*b") == True)
print(s.isMatch("acdcb", "a*c?b") == False)
print(s.isMatch("", "*") == True)
print(s.isMatch("", "****") == True)
print(s.isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab", "***bba**a*bbba**aab**b") == False)
print(s.isMatch("bbbbbbbabbaabbabbbbaaabbabbabaaabbababbbabbbabaaabaab", "b*b*ab**ba*b**b***bba") == False)
print(s.isMatch("bbbbbbbabbaabbabbbbaaabbabbabaaabbababbbabbbabaaabaab", "b*b*ab**ba*b**b***aab") == True)
print(s.isMatch("ab", "?*") == True)
print(s.isMatch("bbaaaabaaaaabbabbabbabbababaabababaabbabaaabbaababababbabaabbabbbbbbaaaaaabaabbbbbabbbbabbabababaaaaa", "******aa*bbb*aa*a*bb*ab***bbba*a*babaab*b*aa*a****") == False)