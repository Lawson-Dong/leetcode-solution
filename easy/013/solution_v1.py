class Solution:
    def romanToInt(self, s: str) -> int:
        roman_number = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000,
        }
        integer = 0

        for i in range(len(s) - 1):
            current_val = roman_number[s[i]]
            next_val = roman_number[s[i + 1]]

            # A smaller value before a larger one is subtracted.
            if current_val < next_val:
                integer -= current_val
            else:
                integer += current_val

        # The final symbol has no next symbol and is always added.
        integer += roman_number[s[len(s) - 1]]
        return integer
