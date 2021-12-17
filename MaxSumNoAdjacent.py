def maxSubsetSumNoAdjacent(array):
	if len(array) == 0:
		return 0
	if len(array) == 1:
		return 1
	maxSumList = [0] * len(array)
	maxSumList[0] = array[0]
	maxSumList[1] = array[1]
	
	for i in range(2,len(array)):
		maxSumList[i] = getMaxSum(maxSumList[:i-1], array[i])
	return max(maxSumList)

def getMaxSum(array, elem):
	jumpFrom1 = len(array) - 1
	jumpFrom2 = len(array) - 2
	max1 = elem + array[jumpFrom1] if jumpFrom1 >= 0 else 0
	max2 =  elem + array[jumpFrom2] if jumpFrom2 >= 0 else 0
	
	
	
	
	return max(max1,max2)

print(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]))