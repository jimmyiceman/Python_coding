# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 21:57:54 2016
Objective: SYS module
@author: jatan.sharma
"""

import sys

sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')

# sys.argv is the list of arguments passed from other program (like shell), first index is 0 and is always reserved for exected file name. Hence we are taking index 1 for the arg
def main(arg):
    print(arg)

main(sys.argv[1])