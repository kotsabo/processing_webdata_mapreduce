#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Oct 15 00:27:51 2017

@author: kotsabo
"""

import sys

key, new_key, string = None, None, ''

for line in sys.stdin:
    line = line.strip()
    tokens = line.split('.')
    new_key = tokens[0]
    print(tokens)
    
    if new_key != key and key != None:
        print(key + ' -->' + string)
        string = ''
    
    if tokens[1] != ' ':
        string += ' ('+ tokens[2] + ',' + tokens[1] + ')'
    key = new_key
    
print(key + ' -->' + string)