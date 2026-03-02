# Calculate the sum of digits of a number
def sum_of_digits(n):
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    return total


num = int(input("Enter number: "))
print("Sum of digits:", sum_of_digits(num))

# Time Complexity: O(log n)
# Space Complexity: O(1)


# | Question       | Time Complexity | Space Complexity |
# | -------------- | --------------- | ---------------- |
# | Count digits   | O(log n)        | O(1)             |
# | Reverse number | O(log n)        | O(1)             |
# | Prime check    | O(√n)           | O(1)             |
# | Armstrong      | O(log n)        | O(1)             |
# | Palindrome     | O(log n)        | O(1)             |
# | Power of two   | O(log n)        | O(1)             |
# | Sum of digits  | O(log n)        | O(1)             |
