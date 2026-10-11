class Solution:
    def mySqrt(self, x: int) -> int:
        # left and right define the current inclusive search interval.
        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                # The answer must be larger than mid.
                left = mid + 1
            else:
                # The answer must be smaller than mid.
                right = mid - 1

        # If no exact square root was found, the boundaries have crossed:
        # left == right + 1. Here right is the largest integer with
        # right * right <= x, i.e., floor(sqrt(x)).
        return right
