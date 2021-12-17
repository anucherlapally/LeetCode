def sunsetViews(buildings, direction):
	viewBuildings = []
	currHeight = 0
	
	if direction == "WEST":
		startIdx, endIdx, step = 0, len(buildings), 1
	else:
		startIdx, endIdx, step = len(buildings) - 1, -1, -1
	
	for i in range(startIdx, endIdx, step):
		if buildings[i] > currHeight:
			viewBuildings.append(i)
			currHeight = buildings[i]
	
	if direction == "EAST":
		startIdx, endIdx = 0, len(viewBuildings) - 1
		while startIdx <= endIdx:
			viewBuildings[startIdx], viewBuildings[endIdx] = viewBuildings[endIdx], viewBuildings[startIdx]
			startIdx += 1
			endIdx -= 1
			
	return viewBuildings

print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], "EAST"))