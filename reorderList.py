class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head):

    
        stack = []

        left, right = head, head
        counter = 0

        while right != None and right.next != None:
            right = right.next.next
            left = left.next
            counter += 1
        
        while left != None:
            temp = left
            left = left.next 
            temp.next = None
            stack.append(temp)

        temp = head
        
        run = 0

        while run < counter - 1:
            temp = temp.next
            run += 1

        temp.next = None
        curr = head

        while curr != None:
            temp = curr.next
            curr.next = stack.pop()
            curr.next.next = temp
            prev = curr.next
            curr = temp


        if len(stack) > 0:
            prev.next = stack.pop()


