# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 00:19:54 2020

@author: lab
"""

def compoundinterest(prin,rate,time):
    prin=int(prin)
    time=int(time)
    rate=float(rate)
    prin=prin*((1+rate/100)**time)
    return prin

print("enter prin rate and time for compund interest")
#prin,rate,time=input().split()
#a=compoundinterest(prin,rate,time)
#print(a)
print(int(x) for x in input().split())
