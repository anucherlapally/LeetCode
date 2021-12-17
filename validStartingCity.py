def validStartingCity(distances, fuel, mpg):
	currCarFuel = 0
	validStartingPoint = 0
	for i in range(len(distances)):
		if currCarFuel < 0:
			currCarFuel = 0
			validStartingPoint = i
		currCarFuel += fuel[i]
		currCarFuel = currCarFuel - ( distances[i] / mpg ) 
	
	if currCarFuel < 0:
		validStartingPoint = -1
		
		
		
		
	return validStartingPoint

distances = [30, 40, 10, 10, 17, 13, 50, 30, 10, 40]
fuel = [1, 2, 0, 1, 1, 0, 3, 1, 0, 1]
mpg = 25
print(validStartingCity(distances, fuel, mpg))