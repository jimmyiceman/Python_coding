# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 17:05:55 2016
Objective: List Vs Tuple
@author: jatan.sharma
"""

def example():
    return 15, 12

x, y = example()
print(x,y)

# in the above case, we have used a tuple and cannot modify it... and
# we definitely do not want to!
myTuple = 5,6,7,89,9
print(myTuple[1])