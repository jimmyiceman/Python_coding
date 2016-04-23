# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 15:13:38 2016
Objective: working with CSVs
@author: jatan.sharma
"""

import csv

dates = []
colors = []

with open('D:/jit/Python_coding/File manipulation/resources/read.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    
    for row in readCSV:
        color = row[3]
        date = row[0]
        
        dates.append(date)
        colors.append(color)
        
    print(dates)
    print(colors)
    
    try:
        whatColor = input('What color do you wish to know the date of?:')
        coldex = colors.index(whatColor)
        theDate = dates[coldex]
        print('The date of',whatColor,'is:',theDate)
    except Exception as e:
        print(e)
