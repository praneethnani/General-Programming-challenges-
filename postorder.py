# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 09:02:34 2014

@author: praneethpuligundla
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of integers
    
    def postorderTraversal(self, root):
        result = []
        stack = [root]
        while len(stack)>0:
            node=stack.pop()
            if node:
                if type(node) == int :
                    result.append(node)
                else:
                    stack.append(node.val)
                    stack.append(node.right)
                    stack.append(node.left)
        return result
       
       