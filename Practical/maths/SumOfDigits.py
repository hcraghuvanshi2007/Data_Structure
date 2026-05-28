class Solution:
    def sumOfDigits(self, n: int) -> int:
        n = abs(n)  # handle negative numbers
        total = 0
        
        while n > 0:
            total += n % 10
            n //= 10
        
        return total