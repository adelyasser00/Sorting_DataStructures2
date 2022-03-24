import time
import random
import numba
import numpy as np


# Use numba to speed up array generation, has no effect on sorting algorithms
@numba.jit(nopython=True)
# Array generation
def genArray(size):
    arr = list(range(size))
    for i in range(size):
        arr[i] = random.randint(0, size * 10)
    return arr


# _____PART 6 FUNCTIONS_____ #
def hybridSort(arr, THRESHOLD):
    if len(arr) > 1:
        # Divide array into two left and right halves
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        # Recursively divide arrays till the THRESHOLD is obtained
        # First case: both left and right arrays are larger than the THRESHOLD
        if len(left) > THRESHOLD and len(right) > THRESHOLD:
            # recursively sort left and right arrays
            hybridSort(left, THRESHOLD)
            hybridSort(right, THRESHOLD)
        # Second case: only one of the divided arrays meets the THRESHOLD
        elif len(left) > THRESHOLD:
            hybridSort(left, THRESHOLD)
        elif len(right) > THRESHOLD:
            hybridSort(right, THRESHOLD)
        # switch to selection sort.
        """
        Optimization: We only need to use selection sort on arrays smaller than
        the THRESHOLD. Hence, when the smallest arrays are sorted and merged,
        we no longer need to perform any selection sorting as current arrays
        would already be sorted therefore shouldn't be sent to selection sort 
        function for time waste, we would only need to merge arrays recursively
        until the original array is full and sorted.
        """
        if len(left) <= THRESHOLD:
            selectionSort(left)
        if len(right) <= THRESHOLD:
            selectionSort(right)
        merge(arr, left, right)


def selectionSort(arr):
    for i in range(len(arr) - 1):
        # default first element of unsorted as minimum each iteration
        iMin = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[iMin]:
                # update minimum position
                iMin = j
        # swap the smallest element in this iteration to its correct position
        if iMin != i:
            arr[iMin], arr[i] = arr[i], arr[iMin]


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


# _____END OF PART 6 FUNCTIONS_____ #

# _____PART 7 FUNCTIONS_____ #
def selectk(nums, start, end, rank):
    if rank <= 1:
        rank += 1
    elif rank > len(nums):
        print('K is out of range for the size!')
        return
    if end == start:
        return nums[end]
    else:
        # Randomly partition an element
        q = partition(nums, start, end)
        # check if partitioned element is the Kth smallest in array
        k = q - start + 1
        if (rank - 1) == k:
            return nums[q]
        # search in the smaller or larger sub-arrays depending on the position
        # of the desired Kth smallest element with respect to the element we just
        # partitioned.
        if (rank - 1) < k:
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


# _____END OF PART 7 FUNCTIONS_____ #

# _____CODE TESTING AREA_____ #
print('part 6(Hybrid Sort):')
test6 = genArray(20)
test7 = test6.copy()
print('Unsorted: ' + str(test6))
THRESHOLD = 6
hybridSort(test6, THRESHOLD)
print('Sorted: ' + str(test6))

print('_______________________')

print('Part 7(Kth smallest element): ')

print(test7)
# Kth smallest, K=2: second smallest, K=1: smallest
# Note: if we put k = 0 or k = 1, it will show smallest
k = 19
result = selectk(test7, 0, len(test7) - 1, k + 1)
print('Kth smallest element ( k=', k, ') is:', result)

# __________End of code__________ #
