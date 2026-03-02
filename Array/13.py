# Move Zeroes
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        pos = 0  # position for non-zero

        for i in range(len(nums)):

            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1

List = [0, 1, 0, 3, 12]
Solution().moveZeroes(List)
print(List)

# Time Complexity: O(n) due to the single pass through the array
# Space Complexity: O(1) since we are modifying the array in place