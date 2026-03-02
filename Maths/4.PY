# Check if a number is an Armstrong number or not
def is_armstrong(n):
    temp = n
    power = len(str(n))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10

    return total == n


num = int(input("Enter number: "))

if is_armstrong(num):
    print("Armstrong Number")
else:
    print("Not Armstrong")

# Time Complexity: O(log n)
# Space Complexity: O(1)