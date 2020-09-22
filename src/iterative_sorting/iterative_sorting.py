import random
# TO-DO: Complete the selection_sort() function below
def selection_sort(arr): #O(n^2)
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(cur_index +1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr




# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr): #O(n^2)
    # Your code here
    # Loop through your array
        # Compare each element to its neighbor
        # If elements in wrong position (relative to each other, swap them)
    # If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
    swap = 1
    while swap > 0:
        swap = 0
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap +=1  
    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr2 = []
arr3 = [0, 1, 2, 3, 4, 5]
arr4 = random.sample(range(200), 50)
print("arr1", bubble_sort(arr1))
print("arr2", bubble_sort(arr2))
print("arr3", bubble_sort(arr3))
print("arr4", bubble_sort(arr4))

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def isNegativeElement(arr):
    negative = False
    for el in arr:
        if el < 0:
            negative = True
    return negative


def counting_sort(arr, maximum=0): #O(n + c)
    if maximum == 0 and arr != []:
        maximum = max(arr)

    if isNegativeElement(arr):
        return "Error, negative numbers not allowed in Count Sort"

    count_arr = [0]*(maximum +1)
    output = [0]*len(arr)

    for i in range(0, maximum + 1):
        count_arr[i] = arr.count(i)
    
    for i in range(0, maximum + 1):
        if i != 0:
            count_arr[i] += count_arr[i-1] 
    
    for i in range(len(arr)):
        output[count_arr[arr[i]] - 1] = arr[i]
        count_arr[arr[i]] -= 1
       
   
    for i in range(0, len(arr)):
        arr[i] = output[i]

    return arr

arr10 = [4,2,2,8,3,3,1]
print("arr10: ",counting_sort(arr10, 8))

arr11 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print("arr11: ",counting_sort(arr11, 9))

arr12 = [1, 5, -2, 4, 3]
print("arr12: ", counting_sort(arr12, 5))