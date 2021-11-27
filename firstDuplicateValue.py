def firstDuplicateValue(array):
	
    for i in range(len(array)):
	    index = abs(array[i])
	    if array[index - 1] < 0:
		    return abs(index)
	    array[index - 1] = - array[index - 1]
	
    return - 1

firstDuplicateValue([2, 1, 5, 2, 3, 3, 4])