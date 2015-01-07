# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 17:19:25 2014

@author: praneethpuligundla
"""

def bulleyes(a,b):
    length_a=len(a)
    length_b=len(b)
    if length_a <length_b:
        range_l=length_a
        eval_p(range_l,a,b)
    else:
         range_l=length_b
         eval_p(range_l,b,a)

def eval_p(range_l,a,b):
    cows=0
    bulls=0
    for i in range(range_l):
        if a[i]==b[i]:
            bulls+=1
        elif a[i] in b:
            cows+=1
    print "bulls: "+str(bulls)+ " cows: " +str(cows)
            

bulleyes("epic","pic")
bulleyes("piceo","picoppp")