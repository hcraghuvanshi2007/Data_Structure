# Check if a number is a palindrome or not
def is_palindrome(n):
    original = n
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10

    return original == rev


num = int(input("Enter number: "))

if is_palindrome(num):
    print("Palindrome Number")
else:
    print("Not Palindrome")

# Time Complexity: O(log n)
# Space Complexity: O(1)