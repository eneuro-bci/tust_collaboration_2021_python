# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 17:55:18 2021

@author: 50301
"""

print("please input a number")
x=int(input())
print("add or mul,1:add 2:mul")
y=int(input())
if y==1:
  a = 0
  for  i in range(0,x):
      a += (i+1)
  print(a)
elif y==2:
    a = 1
    for  i in range(0,x):
       a *= (i+1)
    print(a)
else:
    print("no this number")


