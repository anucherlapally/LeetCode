# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root == None:
            return []

        level_order = []

        queue = [root]

        while len(queue) > 0:
            
            values = []
            new_queue = []
            for elem in queue:
                if elem != None:
                    values.append(elem.val)
                
                if elem.left != None:
                    new_queue.append(elem.left)

                if elem.right != None:
                    new_queue.append(elem.right)

            level_order.append(values)

            queue = new_queue[:]


        return level_order[::-1]

        


