# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 19:31:01 2021

@author: 50301
"""

def pick(n):
    list2=[list1[i] for i in range(0,n,2)]
    print(list2)

list1=[1,2,3,4,5,6,7,8]
pick(8)