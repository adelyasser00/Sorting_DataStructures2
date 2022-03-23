import time
import random

import numba
import numpy as np


# x= np.random.randint(1,100,9)

# @numba.jit(nopython=True)
def genArray(size):
    arr = list(range(size))
    for i in range(size):
        arr[i] = random.randint(0, size*10)
    return arr


# x = [22, 50, 14, 8, 66, 12, 90]


# 8, 12, 14,22, 50, 66, 90

def selectionsort(nums):
    n = len(nums)
    for i in range(0, n - 1):
        indxmin = i
        for j in range(i + 1, n):
            if nums[indxmin] > nums[j]:
                indxmin = j

        if indxmin != i:
            nums[i], nums[indxmin] = nums[indxmin], nums[i]


# @numba.jit(nopython=True)
def insertionsort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        index = i
        while index > 0 and nums[index - 1] > key:
            nums[index] = nums[index - 1]
            index = index - 1

        nums[index] = key


def partitionrandom(nums, start, end):
    if start == end:
        return start

    n = end - start + 1
    pivot = random.randint(0, n - 1)

    nums[0], nums[pivot] = nums[pivot], nums[0]

    lastknown = start
    firstunknown = lastknown + 1

    while firstunknown < n:
        if nums[firstunknown] <= nums[start]:
            lastknown = lastknown + 1
            nums[firstunknown], nums[lastknown] = nums[lastknown], nums[firstunknown]

        firstunknown = firstunknown + 1

    nums[start], nums[lastknown] = nums[lastknown], nums[start]

    return lastknown


def selectk(nums, start, end, rank):
    if (end == start):
        return nums[end]

    else:
        q = partition(nums, start, end)
        k = q - start + 1
        if rank == k:
            return nums[k]
        if rank < k:
            return selectk(nums, start, q - 1, rank)
        else:
            return selectk(nums, q + 1, end, rank - k)


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
    firstUnknown = lastS1 + 1
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


def quickSort(arr, first, last):
    # check sort
    if first < last:
        # partition the random lastS1
        lastS1 = partition(arr, first, last)
        # quick sort the two smaller arrays
        quickSort(arr, first, lastS1 - 1)
        quickSort(arr, lastS1 + 1, last)


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
    leftSize = len(left)
    rightSize = len(right)
    # first case: left and right arrays still have elements
    while iLeft < leftSize and iRight < rightSize:
        if left[iLeft] <= right[iRight]:
            arr[iArr] = left[iLeft]
            iLeft += 1

        else:
            arr[iArr] = right[iRight]
            iRight += 1

        iArr += 1
    """ second case: one of the arrays finished and
     there are still elements in the other """
    while iLeft < leftSize:
        arr[iArr] = left[iLeft]
        iArr += 1
        iLeft += 1
    while iRight < rightSize:
        arr[iArr] = right[iRight]
        iArr += 1
        iRight += 1



# y=x.copy()

# x[0]=-1
# start=time.time()

# mergeSort(y)
# selectionsort(x)

mid1 = time.time()
mid2 = time.time()

#
# print("sorted array")
# mergeSort(y)

# quickSort(y,0,len(x)-1)

# end= time.time()

#
x = genArray(50)
i = 8
print(x)
# y=partition(x,0,49)
y = selectk(x, 0, len(x) - 1, i-1)
print(x)
print(y)
quickSort(x, 0, len(x) - 1)
print(i, "th element is ", x[i-1])
print(x)
