# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)

        return expected - actual


nums = [3, 0, 1]
print(Solution().missingNumber(nums))