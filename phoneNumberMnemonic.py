def phoneNumberMnemonics(phoneNumber):
	hashmap = {0:['0'], 1:['1'], 2:['a','b','c'], 3:['d','e','f'], 
			   4:['g','h','i'], 5:['j','k','l'], 6:['m','n','o'],
			  7:['p','q','r','s'], 8:['t','u','v'], 9:['w','x','y','z']}
	
	stringList = []
	
	for i in range(0, len(phoneNumber)):
		list1 = []
		letters = hashmap[int(phoneNumber[i])]
		if len(stringList) > 0:
			for string in stringList:
				for j in letters:
					letter = string
					letter += (j)
					list1.append(letter)
			stringList = list1
		else:
			for j in letters:
				stringList.append(j)
		
	return stringList

print(phoneNumberMnemonics("1905"))