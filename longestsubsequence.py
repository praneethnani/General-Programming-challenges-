# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 09:22:25 2014

@author: praneethpuligundla
"""


def longestConsecutive(num):
    dict={}
    for each in num:
            dict[each]=1
    max=1

    for each in num:
        count=1
        next_val=each+1
        prev_val=each-1
        while next_val in dict:
            count+=1
            del dict[next_val]
            next_val+=1
        while prev_val in dict:
            count+=1
            del dict[prev_val]
            prev_val-=1
            
        if max<count:
           max=count   
           
    return max
    
num=[1,9,2,22,4,23,24]

longestConsecutive(num)