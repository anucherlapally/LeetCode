def sortStack(stack):
	if len(stack) == 0:
		return []
	
	element = stack.pop()
	
	sortStack(stack)
	
	insertInOrder(stack, element)
	
	return stack

def insertInOrder(stack, element):
	if len(stack) == 0:
		stack.append(element)
		return
	
	if stack[len(stack) - 1] <= element:
		stack.append(element)
		return
	
	top = stack.pop()
	
	insertInOrder(stack, element)
	
	stack.append(top)
	
	return stack
	
	
		
