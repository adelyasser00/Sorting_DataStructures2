import time
import numba
import random
import numpy as np


@numba.jit(nopython=True)
def genArray(size):
    arr = list(range(size))
    for i in range(size):
        arr[i] = random.randint(1, size*10)
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


def selectionsort(nums):
    n = len(nums)
    for i in range(0, n-1):
        indxmin=i
        for j in range(i+1, n):
            if nums[indxmin] > nums[j]:
                indxmin=j

        if indxmin != i:
            nums[i], nums[indxmin] = nums[indxmin], nums[i]

#@numba.jit(nopython=True)
def insertionsort(nums):
    n=len(nums)
    for i in range(1,n):
        key=nums[i]
        index=i
        while index>0 and  nums[index-1] > key:
             nums[index]=nums[index-1]
             index = index - 1

        nums[index] = key


# Timing for each sorting mechanism
lengths = 1000, 25000, 50000, 100000
quicktest = mergetest = selectiontest = insertiontest = genArray(lengths[0])
quicktest1 = mergetest1 = selectiontest1 = insertiontest1 = genArray(lengths[1])
quicktest2 = mergetest2 = selectiontest2 = insertiontest2 = genArray(lengths[2])
quicktest3 = mergetest3 = selectiontest3 = insertiontest3 = genArray(lengths[3])
print('________Quick sort________')
tStart = time.time()
quickSort(quicktest, 0, len(quicktest) - 1)
tEnd = time.time()
print('For 1000: ')
print((str((tEnd - tStart) * 1000)) + ' ms')

tStart = time.time()
quickSort(quicktest1, 0, len(quicktest1) - 1)
tEnd = time.time()
print('For 25000: ')
print((str((tEnd - tStart) * 1000)) + ' ms')

tStart = time.time()
quickSort(quicktest2, 0, len(quicktest2) - 1)
tEnd = time.time()
print('For 50000: ')
print((str((tEnd - tStart) * 1000)) + ' ms')

tStart = time.time()
quickSort(quicktest3, 0, len(quicktest3) - 1)
tEnd = time.time()
print('For 100000: ')
print((str((tEnd - tStart) * 1000)) + ' ms')

print('________Merge Sort________')

tStart = time.time()
mergeSort(mergetest)
tEnd = time.time()
print('For 1000: ')
print((str((tEnd - tStart) * 1000)) + ' ms')

tStart = time.time()
mergeSort(mergetest1)
tEnd = time.time()
print('For 25000: ')
print((str((tEnd - tStart) * 1000)) + ' ms')

tStart = time.time()
mergeSort(mergetest2)
tEnd = time.time()
print('For 50000: ')
print((str((tEnd - tStart) * 1000)) + ' ms')

tStart = time.time()
mergeSort(mergetest3)
tEnd = time.time()
print('For 100000: ')
print((str((tEnd - tStart) * 1000)) + ' ms')

print('________insertion sort________')

tStart = time.time()
insertionsort(insertiontest)
tEnd = time.time()
print('For 1000:')
print((str((tEnd - tStart) * 1000)) + ' ms')

tStart = time.time()
insertionsort(insertiontest1)
tEnd = time.time()
print('For 25000:')
print((str((tEnd - tStart) * 1000)) + ' ms')

tStart = time.time()
insertionsort(insertiontest2)
tEnd = time.time()
print('For 50000:')
print((str((tEnd - tStart) * 1000)) + ' ms')

tStart = time.time()
insertionsort(insertiontest3)
tEnd = time.time()
print('For 100000:')
print((str((tEnd - tStart) * 1000)) + ' ms')

print('________Selection Sort________')


selectionsort(selectiontest)
tEnd = time.time()
print('For 1000: ')
print((str((tEnd - tStart) * 1000)) + ' ms')

selectionsort(selectiontest1)
tEnd = time.time()
print('For 25000: ')
print((str((tEnd - tStart) * 1000)) + ' ms')

selectionsort(selectiontest2)
tEnd = time.time()
print('For 50000: ')
print((str((tEnd - tStart) * 1000)) + ' ms')

selectionsort(selectiontest3)
tEnd = time.time()
print('For 100000: ')
print((str((tEnd - tStart) * 1000)) + ' ms')