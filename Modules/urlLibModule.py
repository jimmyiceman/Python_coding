# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 21:56:32 2016
objective: urllib module
@author: jatan.sharma
"""
import urllib.request

# GET request | this will give you the source code for the website
x = urllib.request.urlopen('http://www.google.com')
print(x.read())

# POST request
import urllib.parse

# base URL
url = 'http://www.imdb.com/'
values = {'ref_':'nv_sr_fn',
         'q':'ted',
         's':'all'}

# This will encode as it should be (all &, ? other encoding on the URL is taken care of)        
data = urllib.parse.urlencode(values)
data = data.encode('UTF-8')

req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()
print(respData)


'''
Some sites block bot access, here how to get around it
'''
# Failure case
try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
except Exception as e:
    print(str(e))
    
try:
    url = 'https://www.google.com/search?q=test'
    myHeaders = {}
    myHeaders['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    
    req = urllib.request.Request(url, headers=myHeaders)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    
    saveFile = open('withHeaders.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print(e)
