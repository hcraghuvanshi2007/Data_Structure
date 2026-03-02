# Find if there exists a pair in the array whose sum is equal to a given target
arr = [2, 7, 11, 15]
target = 9

found = False

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            found = True
            break

if found:
    print("Pair exists")
else:
    print("No pair found")

# Time Complexity: O(n^2)
# Space Complexity: O(1)