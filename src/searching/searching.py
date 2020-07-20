def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    if len(arr) == 0:
        return -1
    
    left = 0
    right = len(arr) -1
    while left <= right:
        pivot = left+ (right - left)//2
        if arr[pivot] > target:
            right = pivot
        if arr[pivot] < target:
            left = pivot
        if arr[pivot] == target:
            return pivot

    return -1  # not found
