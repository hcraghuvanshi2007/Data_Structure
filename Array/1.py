# Print elements at even positions in an array
arr = [10, 20, 30, 40, 50, 60]

for i in range(0, len(arr), 2):
    print(arr[i], end=" ")

# Time Complexity: O(n)
# Space Complexity: O(1)