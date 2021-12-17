def subarraySort(array):
	start = -1
	end = -1
	needSort = False
	for i in range(1,len(array)):
		if array[i -1] > array[i]:
			start = getStart(array, i)
			needSort = True
			break
	if needSort:
		
		for i in range(len(array) - 1, -1, -1):
			if array[i] <= array[start]:
				end = i
				break
		while start >= 0:
			if array[end] <= array[start]:
				start -= 1
			else:
				start += 0
				break
	return [start, end]

def getStart(array, idx):
	num = array[idx]
	idx -= 1
	while idx >= 0:
		if array[idx] <= num:
			return idx
		idx -= 1
		
	return -1


print(subarraySort([2,1]))