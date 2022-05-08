# O(nlogn) time | O(1) space
def nonConstructibleChange(coins):
    # Sort first
    coins.sort()

    currentChangeCreated = 0
    '''
	currentChangeCreated is the consecutive amount of change we can make
	The rule of thumb is:
		1. If the next coin is smaller than or equal to currentChangeCreated + 1, then 
		that you can make any combination of change up to currentChangeCreated + coin
			=> currentChangeCreated += coin
		
		2. If the next coin is greater than currentChangeCreated + 1, then that coin can't
		make a combination of currentChangeCreated + 1
			=> return currentChangeCreated + 1
	'''
    for coin in coins:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1

        currentChangeCreated += coin

    return currentChangeCreated + 1
