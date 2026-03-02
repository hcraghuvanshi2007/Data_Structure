# Plus One
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits)-1, -1, -1):

            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        return [1] + digits


digits = [1, 2, 9]
print(Solution().plusOne(digits))

# Time Complexity: O(n) in the worst case when all digits are 9
# Space Complexity: O(1) if we ignore the output list, otherwise O(n) when all digits are 9 