# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 17:42:04 2016
Objective: File manipulation
@author: jatan.sharma
"""

text = 'Sample Text to Save\nNew line!'

'''
Writing to a file
'''
# notifies Python that you are opening this file, with the intention to write
#saveFile = open('C:/Users/jatan.sharma/Desktop/exampleFile.txt','w')
saveFile = open('D:/jit/Python_coding/File manipulation/resources/exampleFile.txt','w')

# actually writes the information
saveFile.write(text)

# It is important to remember to actually close the file, otherwise it will
# hang for a while and could cause problems in your script
saveFile.close()


''' 
Appending to a file
'''
# so here, generally it can be a good idea to start with a newline, since
# otherwise it will append data on the same line as the file left off.
# you might want that, but I'll use a new line.
# another option used is to first append just a simple newline
# then append what you want. 
appendMe = '\nNew bit of information'

appendFile = open('D:/jit/Python_coding/File manipulation/resources/exampleFile.txt','a')
appendFile.write(appendMe)
appendFile.close()


'''
Reading from files
'''
# similar syntax as you've seen, 'r' for read. You can just throw a .read() at
# the end, and you get:
readMe = open('D:/jit/Python_coding/File manipulation/resources/exampleFile.txt','r').read()
print(readMe)

# this will instead read the file into a python list. 
readMe = open('D:/jit/Python_coding/File manipulation/resources/exampleFile.txt','r').readlines()
print(readMe)