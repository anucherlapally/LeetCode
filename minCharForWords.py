def minimumCharactersForWords(words):
	
	minChar = {}
	for word in words:
		charCount = {}
		for letter in word:
			if letter in charCount:
				charCount[letter] += 1
			else:
				charCount[letter] = 1
		for letter in charCount:
			if letter not in minChar:
				minChar[letter] = charCount[letter]
			elif minChar[letter] < charCount[letter]:
				minChar[letter] = charCount[letter]
	
	minCharArr = []
	
	for char in minChar:
		for i in range(minChar[char]):
			minCharArr.append(char)
	return minCharArr


minimumCharactersForWords(["this", "that", "did", "deed", "them!", "a"])