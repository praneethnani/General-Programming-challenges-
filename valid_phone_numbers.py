# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 21:05:03 2014

@author: praneethpuligundla
"""
import math
def valid_phone_number(num,dis_list):
    num=num-1
    startnum=int(math.pow(10,num))
    lastnum=int(math.pow(10,num+1))
    for i in range(startnum,lastnum):
        if check_valid_phone(i,num,dis_list):
            print i
            
        
def check_valid_phone(phno,num,dis_list):
    firstdigit=phno/(10**num-1)
    fourflag=False
    if firstdigit==4:
        fourflag==True
    count_four=0
    previous=None
    current=None
    while phno > 0:
        digit=phno%10
        current=digit
        phno=phno/10
        if current == previous:
            return False
        if digit in dis_list:
            return False
        if digit==4:
            count_four+=1
        
        previous=current            
    if count_four >= 1 and fourflag == False:
        return False
    return True
    
    
valid_phone_number(4,[2,7,9])