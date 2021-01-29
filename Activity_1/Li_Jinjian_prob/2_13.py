# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 19:59:53 2021

@author: 50301
"""


def fbnq(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end='\t')
        a, b = b, a + b


fbnq(100)
