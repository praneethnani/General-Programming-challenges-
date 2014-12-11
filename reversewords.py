# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 01:42:08 2014

@author: praneethpuligundla
"""

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        if(s.strip()==" "):
            return ""
        else:
            s=s.strip()
            s=re.sub('[ ]+'," ",s)
            s=s.split(" ")
            str=""
            for each in s:
                str+=each[::-1]+" "
            str=str.strip()
            return str[::-1]