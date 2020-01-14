# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 00:14:15 2020

@author: lab
"""

time=int(input("enter years"))
rt=int(input("enter interest rate"))
pr=int(input("enter principle"))
total=pr+pr*(rt/100)*time
print(f" simple interest is {total}")