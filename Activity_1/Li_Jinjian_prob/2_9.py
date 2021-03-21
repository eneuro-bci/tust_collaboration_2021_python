# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 19:47:19 2021

@author: 50301
"""


def merge(list1, list2):
    list1.extend(list2)


list1 = [1, 2, 3, 4]
list2 = ["tom", "jack", "cindy", "mike"]
merge(list1, list2)
print(list1)
