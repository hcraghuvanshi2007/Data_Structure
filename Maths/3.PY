# Check if a number is prime or not
def is_prime(n):

    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


num = int(input("Enter number: "))

if is_prime(num):
    print("Prime Number")
else:
    print("Not Prime")

# Time Complexity: O(√n)
# Space Complexity: O(1)