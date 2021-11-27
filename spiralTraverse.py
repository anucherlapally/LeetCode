def spiralTraverse(array):
	retlist = []
	right = len(array[0]) - 1
	left = 0
	upper = 0
	lower = len(array) -1
	while upper <= lower and left <= right:
		for j in range(right):
			retlist.append(array[i][j])
		for i in range(lower):
			retlist.append(array[i][j])
		
		for j in reversed(range(left)):
			retlist.append(array[i][j])
			
		for i in reversed(range(upper)):
			retlist.append(array[i][j])
		
		upper += 1
		right -= 1
		lower -= 1
		left += 1
	return retlist
	
array = [
    [4, 2, 3, 6, 7, 8, 1, 9, 5, 10],
    [12, 19, 15, 16, 20, 18, 13, 17, 11, 14]
  ]
print(spiralTraverse(array))