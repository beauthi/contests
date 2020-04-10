class Solution:
    def combinations(self, n):
        results = []
        for x in range(pow(2, (n - 1) * 2)):
            to_bin = bin(x)[2:]
            to_bin = "0" * ((n - 1) * 2 - len(to_bin)) + to_bin
            if len([e for e in to_bin if e == "1"]) != (n - 1):
                continue
            result = ""
            c = 1
            for bit in to_bin:
                if bit == "1":
                    result += "("
                    c += 1
                else:
                    result += ")"
                    c -= 1
                if c < 0:
                    break
            if len(result) != (2 * (n - 1)):
                continue
            results.append(result)
        return results

    def generateParenthesis(self, n):
        results = []
        if n == 0:
            return results
        if n == 1:
            return ["()"]
        for combination in self.combinations(n):
            results.append("(" + combination + ")")
        return results

s = Solution()
print(s.generateParenthesis(3))
print(s.generateParenthesis(2))
print(s.generateParenthesis(1))
print(s.generateParenthesis(4))