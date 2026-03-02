# Find the missing number in an array of size n-1 containing distinct numbers from 1 to n
arr = [1, 2, 4, 5]
n = 5

expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)

missing = expected_sum - actual_sum

print("Missing number:", missing)

# Time Complexity: O(n)
# Space Complexity: O(1)