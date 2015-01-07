# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 05:33:54 2014

@author: praneethpuligundla
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head != None:
            present=head
            while present.next!=None:
                next=present.next
                if present.val==next.val and next.next!=None:
                    present.next=next.next
                elif present.val==next.val and next.next==None:
                    present.next=None
                else:
                    present=next
        return head
            