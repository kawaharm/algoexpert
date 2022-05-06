"""
Write a function that takes in a non-empty array of integers that are sorted in
ascending order and returns a new array of the same length with the squares of the
original integers also sorted in ascending order.

Ex.
Input = [1, 2, 3, 4, 5]
Output = [1, 4, 9, 16, 25]

Ex.
Input = [-5, -3, 1, 2, 4]
Output= [1, 4, 9, 16, 25]
"""


def sortedSquaredArray(array):
    # # Use two pointers at each end of array and compare absolute values of each
    # # O(n) time | O(n) space
    smallerValueIdx, largerValueIdx = 0, len(array) - 1
    sortedSquares = [0]*len(array)

    # Outermost values in array will be largest when squared,
    # So add larger values first to sortedSquares
    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedSquares[idx] = smallerValue ** 2
            smallerValueIdx += 1
        else:
            sortedSquares[idx] = largerValue**2
            largerValueIdx -= 1

    return sortedSquares
