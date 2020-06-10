# TO-DO: complete the helper function below to merge 2 sorted arrays
# arrA = [1, 3, 5, 7]
# arrB = [2, 4, 6, 8]

def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Left
    x = 0
    # right
    y = 0
    # new array
    z = 0

    # Your code here
    # This will traverse over both of the arrays
    while x < len(arrA) and y < len(arrB):
        # We need to check if the current element of the first
        # array is smaller than the curr of the second array
        if arrA[x] < arrB[y]:
            merged_arr[z] = arrA[x]
            z = z + 1
            x = x + 1
        else:
            merged_arr[z] = arrB[y]
            z = z + 1
            y = y + 1
    # THESE WHILE LOOPS WILL STORE THE REMAINING ELEMENTS
    while x < len(arrA):
        merged_arr[z] = arrA[x]
        z = z + 1
        x = x + 1
    while y < len(arrB):
        merged_arr[z] = arrB[x]
        z = z + 1
        y = y + 1
    # range returns a sequence of numbers starting at 0
    for x in range(elements):
        print(str(merged_arr[x]))

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
