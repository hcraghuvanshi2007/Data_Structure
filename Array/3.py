# Count occurrences of a given element in an array
arr = [1, 2, 3, 2, 4, 2]
target = 2

count = 0

for x in arr:
    if x == target:
        count += 1

print("Occurrences =", count)

# Time Complexity: O(n)
# Space Complexity: O(1)