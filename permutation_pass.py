# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 06:36:27 2014

@author: praneethpuligundla
"""

     
     
     
def permutation(password):
    if len(password) <1:
        yield password
    else:
        for perm in permutation(password[1:]):
            for i in range(len(password)):
                yield perm[i:]+password[0:1]+perm[:i]
     
elements="12332"
permutation(elements)
for perm in permutation(elements):
    if perm[0] < perm[1] <perm[2]:
        print perm