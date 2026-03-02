# Calculate the sum and product of all elements in an array
arr = [1, 2, 3, 4]

total_sum = 0
product = 1

for x in arr:
    total_sum += x
    product *= x

print("Sum =", total_sum)
print("Product =", product)

# Time Complexity: O(n)
# Space Complexity: O(1)