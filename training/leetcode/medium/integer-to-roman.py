class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""

        M = int(num / 1000)
        num = num % 1000
        result += (M * "M")

        if num in range(400, 500):
            result += "CD"
            num = num - 400
        elif num in range(900, 1000):
            result += "CM"
            num = num - 900
        else:
            D = int(num / 500)
            num = num % 500
            C = int(num / 100)
            num = num % 100
            result += (D * "D" + C * "C")

        if num in range(90, 100):
            result += "XC"
            num = num - 90
        elif num in range(40, 50):
            result += "XL"
            num = num - 40
        else:
            L = int(num / 50)
            num = num % 50
            X = int(num / 10)
            num = num % 10
            result += (L * "L" + X * "X")

        if num == 9:
            result += "IX"
        elif num == 4:
            result += "IV"
        else:
            V = int(num / 5)
            num = num % 5
            I = num
            result += (V * "V" + I * "I")
        return result


s = Solution()
print(s.intToRoman(3) == "III")
print(s.intToRoman(4) == "IV")
print(s.intToRoman(9) == "IX")
print(s.intToRoman(58) == "LVIII")
print(s.intToRoman(1994) == "MCMXCIV")