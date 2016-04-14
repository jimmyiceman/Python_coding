# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 14:39:31 2016
Objective: Statistics module
@author: jatan.sharma
"""

import statistics

example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5]

x = statistics.mean(example_list)
print(x)

y = statistics.median(example_list)
print(y)

z = statistics.mode(example_list)
print(z)

a = statistics.stdev(example_list)
print(a)

b = statistics.variance(example_list)
print(b)