def hasSingleCycle(array):
	numElementsVisited = 0
	currentIdx = 0
	
	while numElementsVisited < len(array):
		if numElementsVisited > 0 and currentIdx == 0:
			return False
		currentIdx = getNextIdx(currentIdx, array)
		numElementsVisited += 1
	
	return currentIdx == 0

def getNextIdx(currentIdx, array):
	jump = array[currentIdx]
	return (currentIdx + jump) % len(array)
	
		
