import time
from random import randint
import numba
import numpy as np

x = [ 22, 50, 14, 8, 66, 12, 90 ]
# 8, 12, 14,22, 50, 66, 90

def partitionrandom(nums):
    n = len(x)
    pivot = randint(0, n - 1)

    nums[0], nums[pivot] = nums[pivot], nums[0]

    lastknown = 0
    firstunknown = lastknown + 1

    while firstunknown < n:
        if nums[firstunknown] <= nums[0]:
            lastknown = lastknown + 1
            nums[firstunknown], nums[lastknown] = nums[lastknown], nums[firstunknown]

        firstunknown = firstunknown + 1

    nums[0], nums[lastknown] = nums[lastknown], nums[0]
    print(x)
    print(lastknown)
    return lastknown


def selectk(nums, start, end, rank):
    if (end <= start):

        return nums[end]
    else:
        q = partitionrandom(nums)
        k = q - start + 1
        if rank == k:
            return nums[k]
        if rank > k:
            return selectk(nums, 0, k, rank)
        else:
            return selectk(nums, k + 1, end, rank - k)


l = partitionrandom(x)
l = selectk(x, 0, len(x), 5)
print(l)

