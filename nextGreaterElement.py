def nextGreaterElement(array):
	greaterElemList = [0] * len(array) 
	stack = []
	for i in range(2 * len(array)-1, -1, -1):
		circularIdx = i % len(array)
		greaterElemList[circularIdx] = getFromStack(stack, array[circularIdx])
		
	return greaterElemList

def getFromStack(stack, elem):

	while len(stack) > 0:
		lastElem = stack[len(stack) - 1]
		if lastElem > elem:
			stack.append(elem)
			return lastElem
		stack.pop()
	stack.append(elem)
	return -1


print(nextGreaterElement([2, 5, -3, -4, 6, 7, 2]))