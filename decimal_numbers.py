# -*- coding: utf-8 -*-
"""
Created on Sat Jan  3 14:00:18 2015

@author: praneethpuligundla
"""

import math

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
        

def fraction(fraction):
    length=len(str(fraction))-2
    if length >4:
        print "length of decimal is more than 4"
    else:
        num=int(fraction*10**length)
        dem=10**length
        gcd_val=gcd(num,dem)
        while gcd_val!=1:
            num/=gcd_val
            dem/=gcd_val
            gcd_val=gcd(num,dem)
        print str(num)+"/"+str(dem)
    
    
fraction(0.39959)