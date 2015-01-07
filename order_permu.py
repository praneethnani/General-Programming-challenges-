# -*- coding: utf-8 -*-
"""
Created on Sat Jan  3 14:24:36 2015

@author: praneethpuligundla
"""

def calculate_perm(length):
    start=97
    end=123 
    arr_w=[]
    result=[]
    for i in range(start,end):
        arr_w.append(chr(i))

    permutations(arr_w,0,length,result)
    
def permutations(arr,index,length,result):
  if len(result)==length:
      print result
  else:
      for i in range(index,len(arr)):
          result.append(arr[i])
          permutations(arr,i+1,length,result)
          result.remove(arr[i])

    
calculate_perm(3)   
    
