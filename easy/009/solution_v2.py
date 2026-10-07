class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Reject negative numbers and nonzero numbers ending in zero.
        # Zero itself is a palindrome.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Optimization: reverse the string directly with slicing,
        # avoiding explicit lists, joining, and integer conversion.
        x_str = str(x)
        return x_str == x_str[::-1]
