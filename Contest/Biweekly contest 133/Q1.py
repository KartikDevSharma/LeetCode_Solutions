class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        for num in nums:
            remainder = num % 3
            if remainder == 1:
                operations += 1  # Add 2 or subtract 1
            elif remainder == 2:
                operations += 1  # Add 1 or subtract 2
        return operations
