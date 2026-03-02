# Check if a number is a power of two or not
def is_power_of_two(n):

    if n <= 0:
        return False

    while n % 2 == 0:
        n //= 2

    return n == 1


num = int(input("Enter number: "))

if is_power_of_two(num):
    print("Power of Two")
else:
    print("Not Power of Two")

# Time Complexity: O(log n)
# Space Complexity: O(1)