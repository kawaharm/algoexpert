def findThreeLargestNumbers(array):
    '''
        Create new array and update order of largest numbers as you traverse input array
        '''

    threeLargest = [None, None, None]
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest


def updateLargest(threeLargest, num):
    # Update and shift numbers down accordingly starting with largest
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)


def shiftAndUpdate(array, num, idx):
    # Until i == idx, shift values left
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        # Shift
        else:
            array[i] = array[i+1]