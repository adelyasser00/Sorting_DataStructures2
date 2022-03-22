import time
import numba
import random
import numpy as np


@numba.jit(nopython=True)
def genArray(size):
    arr = np.zeros(size)
    for i in range(size):
        arr[i] = random.randint(1, 1000000)
    return arr


def quickSort(arr, first, last):
    if (len(arr)==1):
        return arr
    if first == last:
        return arr
    # check sort
    if (first < last):
        # partition the random pivot
        pivot = partition(arr, first, last)
        # quick sort the two smaller arrays
        quickSort(arr, first, pivot - 1)
        quickSort(arr, pivot + 1, last)


def partition(arr, first, last):
    print(first)
    print(last)
    # random pivot position
    pivot = random.randint(0, last - first - 1)
    print(pivot)
    # move the pivot to the start of the array to partition
    while True:
        if pivot != first:
            arr[pivot], arr[first] = arr[first], arr[pivot]
            pivot = first
        # check for element to switch from right to left
        while arr[pivot] <= arr[last] and pivot != last:
            last -= 1
            if pivot == last:
                break
            elif arr[pivot] > arr[last]:
                arr[pivot], arr[last] = arr[last], arr[pivot]
                pivot = last
        # check for element to switch from left to right
        while arr[pivot] >= arr[first] and pivot != first:
            first += 1
            if pivot == first:
                break
            elif arr[pivot] < arr[first]:
                arr[pivot], arr[first] = arr[first], arr[pivot]
                pivot = first
        if pivot!=first and pivot !=last:
            if arr[pivot - 1] < arr[pivot] < arr[pivot + 1]:
                return pivot


test = genArray(10)
lol = len(test) - 1
tStart = time.time()
quickSort(test, 0, lol)
tEnd = time.time()
print(tEnd - tStart)
for v in range(lol):
    print(test[v])
