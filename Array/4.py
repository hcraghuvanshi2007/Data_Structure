# Check if an array is sorted in ascending or descending order
arr = [1, 2, 3, 4]

ascending = True
descending = True

for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        ascending = False
    if arr[i] < arr[i+1]:
        descending = False

if ascending:
    print("Sorted Forward (Ascending)")
elif descending:
    print("Sorted Backward (Descending)")
else:
    print("Not Sorted")

# Time Complexity: O(n)
# Space Complexity: O(1)