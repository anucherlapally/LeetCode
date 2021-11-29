def balancedBrackets(string):
	openBrackets = ['(', '[', '{']
	closeBrackets = [')', ']', '}']
	stack = []
	for i in range(len(string)):
		if string[i] in openBrackets:
			stack.append(string[i])
		elif string[i] in closeBrackets:
			element = stack.pop()
			index = closeBrackets.index(string[i])
			if openBrackets[index] != element:
				return False
	
	if len(stack) != 0:
		return False
	
	return True

print(balancedBrackets("([])(){}(())()()"))