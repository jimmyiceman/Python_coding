# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 00:06:03 2016
Objective: Parse Website data using urllib and re
@author: jatan.sharma
"""

import urllib.request
import re

url = 'http://pythonprogramming.net/parse-website-using-regular-expressions-urllib/'

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()

paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))

for eachp in paragraphs:
    print(eachp)