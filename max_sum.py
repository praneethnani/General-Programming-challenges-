# -*- coding: utf-8 -*-
"""
Created on Sun Jan  4 15:39:44 2015

@author: praneethpuligundla
"""

def great(x,y):
    if x>y :
        return x
    else:
        return y
        
def maxsub(li):
    max_so_far=li[0]
    max_curr=li[0]
    start=0
    end=0
    list_n=[]
    list_n.append(li[0])
    for i in range(1,len(li)):
        max_t=max_so_far
        max_curr=great(li[i],max_curr+li[i])
        max_so_far=great(max_curr,max_so_far)
        if max_curr <= li[i]:
            start=i
        if max_so_far >max_t :
            end=i
    return li[start:end+1]
    
    
maxsub([1,21,11,-7,9,99,9])