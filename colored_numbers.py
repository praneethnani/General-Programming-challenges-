# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 18:47:25 2014

@author: praneethpuligundla
"""

def colorfulnumbers(num):
    num_list=convert_to_list(num)
    products=[]
    for i in range(1,len(num_list)+1):
        for j in range(0,len(num_list)):
            if j+i >len(num_list):
                break
            number=num_list[j:j+i]
            product=reduce(lambda x,y:x*y,number)
            if product in products:
                return False
            products.append(product)
    return True
    
    
def convert_to_list(num):
    num_list=[]
    while (num>0):
        digit=num%10
        num=num/10
        num_list=[digit]+num_list
    return num_list


colorfulnumbers(2498)