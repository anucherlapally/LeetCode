def validIPAddresses(string):
	firstPoint = 1
	secondPoint = 3
	thirdPoint = 5
	maxFirst = 5
	resArray = []
	
	for i in range(3):
		newString = generateSubString(string, firstPoint, secondPoint, thirdPoint)
		if isValidString(newString):
			resArray.append(newString)
		thirdPoint += 1
	
	thirdPoint = 5
	for i in range(3):
		newString = generateSubString(string, firstPoint, secondPoint, thirdPoint)
		if isValidString(newString):
			resArray.append(newString)
		secondPoint += 1
		thirdPoint += 1
	
	secondPoint = 3
	thirdPoint = 5
	for i in range(3):
		newString = generateSubString(string, firstPoint, secondPoint, thirdPoint)
		if isValidString(newString):
			resArray.append(newString)
		firstPoint += 1
		thirdPoint += 1
		secondPoint += 1
	print(resArray)
	

def generateSubString(string, firstPoint, secondPoint, thirdPoint):
	newString = ""
	j = 0
	for i in range(len(string)):
		if firstPoint == j or secondPoint == j or thirdPoint == j:
			newString += "."
			j += 1
		newString += (string[i])
		j += 1
	print(newString)
	return newString

def isValidString(string):
	substring = string.split(".")
	if len(substring) < 4:
		return False

	for part in substring:
		if len(part) == 0:
			return False
		if int(part) > 255:
			return False
		if len(part) > 0 and part.startswith('0'):
			return False 
	return True
validIPAddresses("1921680")