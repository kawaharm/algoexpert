"""
Valid Subsequence
Given two non-empty arrays of integers, write a function that determines 
whether the second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent 
in the array but that are in the same order as they appear in the array.
"""


def isValidSubsequence(array, sequence):
    # O(n) tine | O(1) space where n is the length of the array
    arrIdx, seqIdx = 0, 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)
