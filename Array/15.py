# Rotate an array to the right by k steps
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        k = k % len(nums)

        nums[:] = nums[-k:] + nums[:-k]


nums = [1, 2, 3, 4, 5]
k = 2

print("Before: ", nums)
Solution().rotate(nums, k)
print("After:  ", nums)

# Time Complexity: O(n) due to slicing and concatenation
# Space Complexity: O(n) due to the new list created by slicing and concatenation