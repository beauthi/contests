class Solution:
    def myPowRec(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1 / (x * self.myPowRec(x, - n - 1))
        return x * self.myPowRec(x, n - 1)
    def firstSolution(self, x: float, n: int) -> float:
        return round(self.myPowRec(x, n), 5)
    def myPow(self, x:float, n: int) -> float:
        if n == 0:
            return 1
        m = False
        if n < 0:
            n = - n
            m = True
        o = False
        if x < 0:
            x = - x
            o = True
        res = x
        prev = res
        for _ in range(1, n):
            res = res * x
            if prev == res:
                break
            prev = res
        if m:
            res = 1 / res
        if o and (n % 2) != 0:
            res = - res
        return round(res, 5)

s = Solution()
print(s.myPow(2.00000, 10) == 1024.00000)
print(s.myPow(2.10000, 3) == 9.26100)
print(s.myPow(2.00000, -2) == 0.25000)
print(s.myPow(8.88023, 3) == 700.28148)
print(s.myPow(1.00001, 123456) == 3.43684)
print(s.myPow(0.00001, 2147483647) == 0.0)
print(s.myPow(-1.00000, 2147483647) == -1.0)