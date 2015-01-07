# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 15:58:33 2014

@author: praneethpuligundla
"""

def mountain(m):
    if m == [[]]:
        return "null"
    columnlength=len(m[0])
    rowlength=len(m)
    
    for i in range(1,rowlength-1):
        for j in range(1,columnlength-1):
            if m[i][j] > m[i][j-1] and m[i][j]>m[i-1][j] and m[i][j]>m[i-1][j-1] and m[i][j]>m[i-1][j+1] and m[i][j]>m[i][j+1] and m[i][j]>m[i+1][j+1] and m[i][j]>m[i+1][j] and m[i][j]>m[i+1][j-1]:
                    print m[i][j]
                    
m=[[1,2,3],[4,100,5],[6,7,8]]
m=[[1,2,3,6],[4,10,150,4],[6,7,11,12]] 

m=[[1,2,3,6,0,2],[4,10,1,3,4,1],[6,7,1,12,1,1],[10,2,4,30,3,1],[1,1,1,1,1,1]] 
                 
mountain(m)