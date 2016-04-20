# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 18:05:31 2016
Objective: List manipulation
@author: jatan.sharma
"""

# first we need an example list:
x = [1,6,3,2,6,1,2,6,7]
# lets add something.
# we can do .append, which will add something to the end of the list, like:
x.append(55)
print(x)

# Insert in between
x.insert(2,33)
print(x)

# Remove element from the list
x.remove(6)
print(x)

print(x[5])
print(x.index(1))
print(x.count(1))
  
x.sort()
print(x)