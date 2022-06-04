# O(n^2) time | O(n) space
def threeNumberSum(array, targetSum):
    # Sort array
    array.sort()

    output = []

    for i in range(len(array)):
        print("Loop: ", i)
        current = array[i]
        left = i+1
        right = len(array) - 1

        if current >= targetSum:
            break

        while left < right:
            currentSum = current + array[left] + array[right]

            if currentSum > targetSum:
                print("Greater")
                right -= 1
                print("right: ", right)
            elif currentSum < targetSum:
                print("Less")
                left += 1
                print("left: ", left)
            else:
                print("3")
                output.append([current, array[left], array[right]])
                right -= 1
                left += 1

    return output
