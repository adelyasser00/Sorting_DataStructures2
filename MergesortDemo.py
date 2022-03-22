import numba
import random
import numpy as np

@numba.jit(nopython=True)
def genArray(size):
    arr = list(range(size))
    for i in range(size):
        arr[i] = random.randint(0, 100)
    return arr


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        # recursively sort left and right arrays
        mergeSort(left)
        mergeSort(right)
        merge(arr, left, right)


def merge(arr, left, right):
    # merging smaller arrays
    # create indexes for all arrays
    iArr = iLeft = iRight = 0
    # first case: left and right arrays still have elements
    while iLeft < len(left) and iRight < len(right):
        if left[iLeft] < right[iRight]:
            arr[iArr] = left[iLeft]
            iLeft += 1
        else:
            arr[iArr] = right[iRight]
            iRight += 1
        iArr += 1
    """ second case: one of the arrays finished and
     there are still elements in the other """
    while iLeft < len(left):
        arr[iArr] = left[iLeft]
        iArr += 1
        iLeft += 1
    while iRight < len(right):
        arr[iArr] = right[iRight]
        iArr += 1
        iRight += 1


test = genArray(10)
print(test)
mergeSort(test)
print(test)
