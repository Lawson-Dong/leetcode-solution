class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes. A nonzero number
        # ending in zero would need a leading zero after reversal.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Convert the number into individual digit characters.
        x_string = str(x)
        x_list = list(x_string)
        x_list_reversed: list[str] = []

        # Build a new list containing the digits in reverse order.
        for digit in reversed(x_list):
            x_list_reversed.append(digit)

        # Reconstruct the reversed number and compare it with the input.
        x_string_reversed = "".join(x_list_reversed)
        x_reversed = int(x_string_reversed)
        return x == x_reversed
