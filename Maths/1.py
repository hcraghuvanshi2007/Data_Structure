# Count the number of digits in a given number
def count_digits(n):
    count = 0

    while n > 0:
        n //= 10
        count += 1

    return count


num = int(input("Enter number: "))
print("Digits:", count_digits(num))

# Time Complexity: O(log n)
# Space Complexity: O(1)