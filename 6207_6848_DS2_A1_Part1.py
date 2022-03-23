import time
import numba
import random
import numpy as np


# Array generation
@numba.jit(nopython=True)
def genArray(size):
    arr = list(range(size))
    for i in range(size):
        arr[i] = random.randint(1, 1000000)
    return arr


# _________ Quick Sort Algorithm __________ #

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
        return
    # choosing a random pivot
    pivot = random.randint(first, last)
    if pivot != first:
        arr[pivot], arr[first] = arr[first], arr[pivot]
        pivot = first
    # pivot is only and first known element, start unknown at second element
    unknown = first + 1
    while unknown <= last:
        # traversing all unknown elements till the end of the array
        if arr[unknown] <= arr[first]:
            # shift pivot position to the right as we found elements smaller to be on its left
            pivot += 1
            arr[unknown], arr[pivot] = arr[pivot], arr[unknown]
        # shift all elements to the right and reduce unknown elements size by 1
        unknown += 1
        # swap the pivot to its correct place
    arr[first], arr[pivot] = arr[pivot], arr[first]
    return pivot


# __________ Merge Sort Algorithm __________ #

def mergeSort(arr):
    if len(arr) > 1:
        # recursively divide to left and right arrays till one element arrays
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        # recursively sort left and right arrays
        mergeSort(left)
        mergeSort(right)
        merge(arr, left, right)


def merge(arr, left, right):
    # merging smaller arrays
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


# __________ Selection Sort Algorithm __________ #

def selectionsort(nums):
    n = len(nums)
    for i in range(0, n - 1):
        indxmin = i
        for j in range(i + 1, n):
            if nums[indxmin] > nums[j]:
                indxmin = j

        if indxmin != i:
            nums[i], nums[indxmin] = nums[indxmin], nums[i]


# __________ Insertion Sort Algorithm ___________ #

def insertionsort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        index = i
        while index > 0 and nums[index - 1] > key:
            nums[index] = nums[index - 1]
            index = index - 1

        nums[index] = key
    return nums


# Timing for each sorting mechanism
lengths = [1000, 25000, 50000, 100000]
for k in range(len(lengths)):
    quicktest = genArray(lengths[k])
    mergetest = quicktest.copy()
    selectiontest = quicktest.copy()
    insertiontest = quicktest.copy()

    tStart = time.time()
    quickSort(quicktest, 0, len(quicktest) - 1)
    tEnd = time.time()
    print('______Array of ' + str(lengths[k]) + ' numbers______')
    print('Running time for Quick Sort is ')
    print((str((tEnd - tStart) * 1000)) + ' ms')

    tStart = time.time()
    mergeSort(mergetest)
    tEnd = time.time()
    print('Running time for Merge Sort is ')
    print((str((tEnd - tStart) * 1000)) + ' ms')

    tStart = time.time()
    selectionsort(selectiontest)
    tEnd = time.time()
    print('Running time for Selection Sort is ')
    print((str((tEnd - tStart) * 1000)) + ' ms')

    tStart = time.time()
    insertionsort(insertiontest)
    tEnd = time.time()
    print('Running time for Insertion Sort is ')
    print((str((tEnd - tStart) * 1000)) + ' ms')

# __________End of Code___________ #