    # -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 10:14:41 2014

@author: praneethpuligundla
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # @param two ListNodes
    # @return the intersected ListNode  
    def getIntersectionNode(self, headA, headB):
        if headA ==None or headB==None:
            return None
        la=self.get_length(headA)
        lb=self.get_length(headB)
        diff=abs(la-lb)
        if la > lb:
            i=0
            while i<diff:
                i+=1
                headA=headA.next
            while headA!=None or headB!=None:
                if(headA.val==headB.val):
                    return headA
                else:
                    headA=headA.next
                    headB=headB.next
            if headA==None or headB==None:
                return None
        else: 
            i=0
            while i<diff:
                i+=1
                headB=headB.next
            while headA!=None or headB!=None:
                if(headA.val==headB.val):
                    return headA
                else:
                    headA=headA.next
                    headB=headB.next
            if headA==None or headB==None:
                return None 
        
    def get_length(self,l_list):
        count=1
        while(l_list!=None):
            count+=1
            l_list=l_list.next
        return count
