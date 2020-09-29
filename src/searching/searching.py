def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i


    return -1   # not found
# arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
# arr2 = []
# print(linear_search(arr1, 6))
# print(linear_search(arr1, -6))
# print(linear_search(arr1, 0))
# print(linear_search(arr2, 3))

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    start = 0
    end = len(arr) - 1
    
    found = -1
    while start <= end and found < 0:
        middle = (start + end) // 2
        if arr[middle] == target:
            found = middle
            return found
        if arr[middle] > target:
            end = middle -1
        if arr[middle] < target: 
            start = middle +1

    return found 

arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print(binary_search(arr1,-8)) 
