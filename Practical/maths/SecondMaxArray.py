from typing import List
import ast

class Solution:
    def secondMax(self, nums: List[int]) -> int:
        unique = list(set(nums))  # remove duplicates
        
        if len(unique) < 2:
            return -1
        
        unique.sort()
        return unique[-2]