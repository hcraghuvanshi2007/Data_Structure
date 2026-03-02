# Find the duplicate element in an array
arr = [1, 3, 4, 2, 2]

seen = set()

for x in arr:
    if x in seen:
        print("Duplicate:", x)
        break
    seen.add(x)

# Time Complexity: O(n) due to the single pass through the array
# Space Complexity: O(n) in the worst case when all elements are distinct