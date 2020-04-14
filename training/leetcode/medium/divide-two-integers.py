class Solution:
    def firstSolution(self, dividend: int, divisor: int) -> int:
        counter = 0
        acc = 0
        if dividend < 0 and divisor < 0:
            different_signs = False
        elif dividend < 0 and divisor > 0:
            different_signs = True
        elif divisor > 0 and divisor > 0:
            different_signs = False
        else:
            different_signs = True

        if divisor != 1 and divisor != -1:
            while acc <= abs(dividend):
                acc += abs(divisor)
                counter += 1
        else:
            if divisor < 0:
                dividend = - dividend
            if dividend > (pow(2, 31) - 1) or dividend < pow(-2, 31):
                return pow(2, 31) - 1
            else:
                return dividend

        if counter > (pow(2, 31) - 1) or counter < pow(-2, 31):
            return pow(2, 31) - 1
        if different_signs:
            if divisor < 0:
                return - counter + 1
            else:
                return counter + 1
        else:
            return counter - 1
    
    def divide(self, n: int, d: int) -> int:
        MIN_Q = -(1 << 31)
        MAX_Q = (1 << 31) - 1
        sign = -1 if ((n < 0 and d > 0) or (d < 0 and n > 0)) else 1
        
        s = [(abs(d), 1)]
        while len(s) < 33:
            v, i = s[-1]
            s.append((v + v, i + i))

        n = abs(n)
        q = 0
        while len(s) > 0:
            v, i = s.pop()
            if v <= n:
                print(v)
                if sign > 0:
                    q += i
                else:
                    q -= i
                n -= v
        return q if MIN_Q <= q <= MAX_Q else MAX_Q

s = Solution()
print(s.divide(15, 2) == 7)
exit()
print(s.divide(10, 3) == 3)
print(s.divide(7, 3) == 2)
print(s.divide(1, -1) == -1)
print(s.divide(-1, 1) == -1)
print(s.divide(7, -3) == -2)
print(s.divide(-2147483648, -1) == 2147483647)