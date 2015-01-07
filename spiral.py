# -*- coding: utf-8 -*-
"""
Created on Sun Jan  4 19:26:44 2015

@author: praneethpuligundla
"""

def spiral(m,length,columnlength):
    j=columnlength
    i=0
    count=0
    while(i<length):
        while(j>=count):
            print m[i][j]
            j-=1
        i+=1
        j+=1
        while(i<=length):
            print m[i][j]
            i+=1
        j+=1
        i-=1
        while j <=columnlength:
            print m[i][j]
            j+=1
        j-=1
        i-=1

        while i >count:
            print m[i][j]
            i-=1
        count+=1
        length-=1
        columnlength-=1
        j=columnlength
        i=count
    
    

matrix=[['C','I','P','E'], 
['R','N','K','U'], 
['U','O','W','O'], 
['L','E','S','Y']] 

matrix1=[['C','I','P','E','*'], 
['R','N','K','*','U'], 
['U','O','W','*','O'], 
['L','E','S','*','Y']]
 
spiral(matrix1,3,4)