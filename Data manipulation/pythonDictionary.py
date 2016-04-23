# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 19:25:41 2016
Onjective: Python dictionary
@author: jatan.sharma
"""
'''
One of the most useful data types in python is the python
dictionary.

If you are familiar with other languages, think of it like an associative
array. 

The idea of the dictionary is to have what are called keys and values. Despite
being ordered if you print a dictionary out, there is no actual
order to dictionaries.

All keys are unique

So before we used two lists and assumed their association, searched for index,
and found information about 1 item in 1 list from another.

Now here, everything is contained in the same location, and makes more sense

Let us show an example:

'''

# Dictionary of names and ages. 
exDict = {'Jack':15,'Bob':22,'Alice':12,'Kevin':17}

print(exDict)

# How old is Jack
print(exDict['Jack'])

exDict['Tim'] = 15
print(exDict)

del exDict['Tim']
print(exDict)


exDict = {'Jack':[15,'blonde'],'Bob':[22, 'brown'],'Alice':[12,'black'],'Kevin':[17,'red']}
print(exDict['Jack'][1])
