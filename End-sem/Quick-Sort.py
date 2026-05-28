def quicksort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = []
    right = []

    for i in arr[1:]:

        if i < pivot:
            left.append(i)

        else:
            right.append(i)

    return quicksort(left) + [pivot] + quicksort(right)


arr = [35, 10, 50, 25, 5, 40, 15]

print("Original Array:")
print(arr)

sorted_array = quicksort(arr)

print("Sorted Array:")
print(sorted_array)