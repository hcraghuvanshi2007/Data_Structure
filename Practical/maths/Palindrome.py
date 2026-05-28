class Solution:
    def isPalindrome(self, n: int) -> bool:
        if n < 0:
            return False
        
        original = n
        reverse = 0
        
        while n > 0:
            digit = n % 10
            reverse = reverse * 10 + digit
            n //= 10
        
        return original == reverse