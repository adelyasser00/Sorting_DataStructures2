import time
import numba
import random
import numpy as np


@numba.jit(nopython=True)
def genArray(size):
    arr = np.zeros(size)
    for i in range(size):
        arr[i] = random.randint(0, 1000)
    return arr


def quickSort(arr, first, last):
    # check sort
    if first < last:
        # partition the random pivot
        pivot = partition(arr, first, last)
        # quick sort the two smaller arrays
        quickSort(arr, first, pivot - 1)
        quickSort(arr, pivot + 1, last)

def partition(arr, first, last):
    # Generate random pivot position
    if first == last:
        return first
    # choosing a random pivot
    pivot = random.randint(first, last)
    if pivot != first:
        arr[pivot], arr[first] = arr[first], arr[pivot]
        pivot = first
    # pivot is only and first known element,
    # start unknown at second element
    unknown = first + 1
    while unknown <= last:
        # traversing all unknown elements till the end of the array
        if arr[unknown] <= arr[first]:
            # shift pivot position to the right as we found elements
            # smaller to be on its left
            pivot += 1
            arr[unknown], arr[pivot] = arr[pivot], arr[unknown]
        # shift all elements to the right and reduce unknown
        # elements size by 1
        unknown += 1
        # swap the pivot to its correct place
    arr[first], arr[pivot] = arr[pivot], arr[first]
    return pivot


#test = genArray(10)
test= [2, 6, 4, 7, 13, 5, 77, 12, 59, 65]
print(test)
quickSort(test, 0, len(test)-1)
print(test)
