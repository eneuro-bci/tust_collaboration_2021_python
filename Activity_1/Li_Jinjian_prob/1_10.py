# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 19:06:51 2021

@author: 50301
"""
print("input now year")
nowyear=int(input())
yEnd=9999

n=0

for x in range(nowyear,yEnd+1):
   if x%4==0:
      if x%100!=0 or x%400==0:
         print(x,end='\t')
         n=n+1
   if n%5==0:
      print()
   if n>=20:
       break