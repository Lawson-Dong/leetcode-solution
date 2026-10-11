class Solution:
    def mySqrt(self, x: int) -> int:
        n = 0
        while n * n < x:
            n += 1

        if n * n == x:
            return n
        return n - 1
