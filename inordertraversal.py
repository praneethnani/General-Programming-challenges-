# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
        
    def inorderTraversal(self, root):
       stack=[]
       out=[]
       while True:
           while root:
                stack.append(root)
                root=root.left
           if stack == []:
               break
           node=stack.pop()
           out.append(node.val)
           root=node.right
       return out