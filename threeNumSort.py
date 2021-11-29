def threeNumberSort(array, order):
	lastSort = 0
	for i in range(2):
		left = lastSort 
		right = len(array) - 1
		numToSort = order[i]
		while left <= right:
			if array[left] != numToSort and array[right] == numToSort:
				array[left],array[right] = array[right], array[left]
				left += 1
				right -= 1
			elif array[left] == numToSort:
				left += 1
				
			elif array[right] != numToSort:
				right -= 1
			lastSort = left
	return array