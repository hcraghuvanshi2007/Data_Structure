# Print distinct elements in an array
arr = [1, 2, 2, 3, 4, 4, 5]

distinct = []

for i in arr:
    if i not in distinct:
        distinct.append(i)

print("Distinct elements:", distinct)

# Time Complexity: O(n^2) due to the 'in' check in the list
# Space Complexity: O(n) in the worst case when all elements are distinct