class Solution:
    def isValid(self, s):
        l = list()
        for c in s:
            if c == '(' or c == '{' or c == '[': 
                l.append(c)
            else:
                if (c == ')' or c == '}' or c == ']') and len(l) == 0:
                    return False
                if c == ')' and l[-1] != '(':
                    return False
                elif c == '}' and l[-1] != '{':
                    return False
                elif c == ']' and l[-1] != '[':
                    return False
                else:
                    l.pop()
        return l == []