# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 14:39:31 2016
Objective: impoting module syntax
@author: jatan.sharma
"""

example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5]

# Basic Importing
import statistics
print(statistics.mean(example_list))

# Sometimes, however, you will see people use the "as" statement in their imports. This will allow you to basically rename the module to whatever you want. People generally do this to shorten the name of the module. Matplotlib.pyplot is often imported as plt and numpy is often imported as np
import statistics as s
print(s.mean(example_list))

#You can just import each function within the module you plan to use
from statistics import mean

# so here, we've imported the mean function only.
print(mean(example_list))

# and again we can do as
from statistics import mean as m
print(m(example_list))

from statistics import *
print(mean(example_list))