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
        # partition the random lastS1
        lastS1 = partition(arr, first, last)
        # quick sort the two smaller arrays
        quickSort(arr, first, lastS1 - 1)
        quickSort(arr, lastS1 + 1, last)

def partition(arr, first, last):
    # Generate random lastS1 position
    if first == last:
        return first
    # choosing a random lastS1
    lastS1 = random.randint(first, last)
    if lastS1 != first:
        arr[lastS1], arr[first] = arr[first], arr[lastS1]
        lastS1 = first
    # lastS1 is only and first known element,
    # start firstUnknown at second element
    firstUnknown = first + 1
    while firstUnknown <= last:
        # traversing all firstUnknown elements till the end of the array
        if arr[firstUnknown] <= arr[first]:
            # shift lastS1 position to the right as we found elements
            # smaller to be on its left
            lastS1 += 1
            arr[firstUnknown], arr[lastS1] = arr[lastS1], arr[firstUnknown]
        # shift all elements to the right and reduce firstUnknown
        # elements size by 1
        firstUnknown += 1
        # swap the lastS1 to its correct place
    arr[first], arr[lastS1] = arr[lastS1], arr[first]
    return lastS1


#test = genArray(10)
test= [2, 6, 4, 7, 13, 5, 77, 12, 59, 65]
print(test)
quickSort(test, 0, len(test)-1)
print(test)
