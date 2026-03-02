# Find the most frequent element in an array
arr = [1, 2, 2, 3, 3, 3, 4]

freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1

most = max(freq, key=freq.get)

print("Most Frequent:", most)

# Time Complexity: O(n) due to the single pass through the array
# Space Complexity: O(n) in the worst case when all elements are distinct