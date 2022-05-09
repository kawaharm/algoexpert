# Iterative search
# O(logn) time | O(1) space
def binarySearch(array, target):
    # Use binary search algorithm
    start, end = 0, len(array) - 1

    while start <= end:
        mid = (start + end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

# Recursive search
# O(Log(n)) time | O (Log(n)) space bc of recursions on call stack


def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)


def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    potentialMatch = array[mid]
    if target == potentialMatch:
        return mid
    elif target < potentialMatch:
        return binarySearchHelper(array, target, left, mid-1)
    else:
        return binarySearchHelper(array, target, mid + 1, right)
