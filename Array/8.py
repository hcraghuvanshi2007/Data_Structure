# Find the second smallest and second largest elements in an array
arr = [5, 2, 8, 1, 9, 3]

arr.sort()

second_smallest = arr[1]
second_largest = arr[-2]

print("Second Smallest:", second_smallest)
print("Second Largest:", second_largest)

# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1) if we sort in place, otherwise O(n) due to the space used by the sorting algorithm
