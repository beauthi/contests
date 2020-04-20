class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l = []
        for index, digit1 in enumerate(num1[::-1]):
            number = 0
            q = 0
            mult = 10 ** index
            for digit2 in num2[::-1]:
                d1 = ord(digit1) - ord('0')
                d2 = ord(digit2) - ord('0')
                s = (d1 * d2 + q)
                q = ord(str(s / 10).split(".")[0][0]) - ord('0')
                number = number + (s % 10) * mult
                mult *= 10
            number = number + q * mult
            l.append(number)
        return str(sum(l))

s = Solution()
print(s.multiply("2", "3") == "6")
print(s.multiply("123", "456") == "56088")