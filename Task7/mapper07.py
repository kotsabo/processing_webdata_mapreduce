#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Oct 14 23:52:12 2017

@author: kotsabo
"""

import sys

for line in sys.stdin:
    tokens_final = list()
    line = line.strip()
    tokens = line.split(' ')
    
    for token in tokens:
        if token != '':
            tokens_final.append(token)
    
    if tokens[0] == 'student':
        print(tokens_final[1] + '. . ')
        continue
        
    print("{0}.{1}.{2}".format(tokens_final[1],tokens_final[2],tokens_final[3]))
