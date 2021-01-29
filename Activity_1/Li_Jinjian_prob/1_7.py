# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 18:56:36 2021

@author: 50301
"""

for a in range(1, 10):
    for b in range(1, a + 1):
        print('{}*{}={}\t'.format(b, a, a * b), end='')
    print()
