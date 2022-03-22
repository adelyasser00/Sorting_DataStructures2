import numba
import random


@numba.jit(nopython=True)
def genArray(size):
    arr = list(range(size))
    for i in range(size):
        arr[i] = random.randint(0, 1000)
    return arr


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


test = genArray(20)
print('Unsorted array=\t' + str(test))
THRESHOLD = 6
hybridSort(test, THRESHOLD)
print('Sorted array=\t' + str(test))
