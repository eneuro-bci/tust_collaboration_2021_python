# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 19:51:05 2021

@author: 50301
"""


def merge_sort(list1, list2):
    list1.extend(list2)
    list1.sort()


list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
merge_sort(list1, list2)
print(list1)
