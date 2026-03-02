# Reverse a given number
def reverse_number(n):
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10

    return rev


num = int(input("Enter number: "))
print("Reverse:", reverse_number(num))

# Time Complexity: O(log n)
# Space Complexity: O(1)