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
    if len(arr) > 1:
        #This will find the middle
        middle = len(arr)//2
        #Dividing the array elements
        left = arr[:middle]
        #Splits into 2 halves
        right = arr[middle:]

        merge_sort(left)
        merge_sort(right)

        x = y = z = 0
        #This will copy data over int the temoprary array
        while x < len(left) and y < len(right):
            if left[x] < right[y]:
                arr[z] = left[x]
                x += 1
            else:
                arr[z] = right[y]
                y += 1
            z += 1
        #Checks all the remainder
        while x < len(left):
            arr[z] = left[x]
            x += 1
            z += 1
        while y < len(right):
            arr[z] = right[y]
            y += 1
            z += 1

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
