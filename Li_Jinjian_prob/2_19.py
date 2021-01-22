# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 20:11:55 2021

@author: 50301
"""

def bot(list1):
    size = len(max(list1, key=len))
    print('*' * (size + 4))
    for word in list1:
        print('* {a:<{b}} *'.format(a=word, b=size))
    print('*' * (size + 4))
    
list1 = ["Hello", "World", "in", "a", "frame"]

bot(list1)