class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Map each previously visited number to its index.
        seen_indices: dict[int, int] = {}

        for index in range(len(nums)):
            current_num = nums[index]
            complement = target - current_num

            # Look up the complement before storing the current number
            # so that the same array element cannot be used twice.
            if complement in seen_indices:
                return [seen_indices[complement], index]

            # Save the current number for subsequent complement checks.
            seen_indices[current_num] = index

        # Unreachable for valid inputs: exactly one solution is guaranteed.
        return []
