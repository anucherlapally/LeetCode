# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
	curr = linkedList
	prev = linkedList
	
	while curr != None:
		print(curr.value)
		temp = curr.next
		while prev != None and temp != None and temp.value == prev.value:
			temp = temp.next
			
		print(curr.value)
		curr.next = temp
		prev = temp
		curr = temp
	
	return linkedList

linkedList = LinkedList(1)
linkedList.next = LinkedList(1)
linkedList.next.next = LinkedList(3)
linkedList.next.next.next = LinkedList(4)
linkedList.next.next.next.next = LinkedList(4)
linkedList.next.next.next.next.next = LinkedList(4)
linkedList.next.next.next.next.next.next = LinkedList(5)
linkedList.next.next.next.next.next.next.next = LinkedList(6)
linkedList.next.next.next.next.next.next.next.next = LinkedList(6)

print(removeDuplicatesFromLinkedList(linkedList))