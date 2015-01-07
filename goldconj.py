# -*- coding: utf-8 -*-
"""
Created on Sat Jan  3 22:03:12 2015

@author: praneethpuligundla
"""
import math
def goldconj(number):
    if number > 2 and number%2 ==0:
        for i in range(2,number/2):
            if isprime(i) and isprime(number-i):
               print str(i)+","+str(number-i)
             
def isprime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True
    
    
goldconj(100)