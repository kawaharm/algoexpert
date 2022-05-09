"""
You're given the head of a Singly Linked List whose nodes are in sorted order with respect
to their values. Write a function that returns a modified version of the linked list that
doesn't contain any nodes with duplicate values. 

Linked list should be modified in place and still be sorted afterwards.

Ex.
linkedList = 1 -> 1 -> 3 -> 3 -> 4 -> 5 -> 5 -> 5 -> 5
output = 1 -> 3 -> 4 -> 5 
"""

# This is an input class. Do not edit.


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time | O(1) space


def removeDuplicatesFromLinkedList(linkedList):
    # Create two pointers: current node and next distinct node
    currentNode = linkedList
    while currentNode is not None:
        # Set pointer after current node
        nextDistinctNode = currentNode.next
        # Move pointer until next distinct node
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
            nextDistinctNode = nextDistinctNode.next

        currentNode.next = nextDistinctNode
        currentNode = nextDistinctNode

    return linkedList
