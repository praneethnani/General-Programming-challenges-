class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class binarytree:
    def binarytree(self,root):
        
    


class Solution:
    # @param root, a tree node
    # @return a list of integers
    ama=[]
    def inorderTraversal(self, root):
        global ama
        if root!=None:
            self.inorderTraversal(root.left)
            self.ama.append(root.val)
            self.inorderTraversal(root.right)
        return self.ama