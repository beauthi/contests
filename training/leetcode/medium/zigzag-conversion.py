class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if s == "" or numRows < 2:
            return s
        result = ""
        limit = 2 * (numRows - 1)
        steps = range(limit, 0, -2)
        for row_number in range(numRows):
            indexes = [limit - steps[row_number % len(steps)], steps[row_number % len(steps)]]
            indexes = [index for index in indexes if index != 0]
            index = row_number
            iterator = 0
            while index < len(s):
                result += s[index]
                iterator += 1
                index = index + indexes[iterator % len(indexes)]
        return result

s = Solution()
print(s.convert("PAYPALISHIRING", 1))
print(s.convert("PAYPALISHIRING", 2))
print(s.convert("PAYPALISHIRING", 3))
print(s.convert("PAYPALISHIRING", 4))
