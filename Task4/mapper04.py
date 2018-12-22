#!/usr/bin/python3

"""
Created on Tue Oct 10 17:57:02 2017
@author: kotsabo
"""

import sys
import re

for line in sys.stdin:
    tokens_final = list()
    tokens = re.split('\n| |\t|\r|\f',line)
    for token in tokens:
        if token != '':
            tokens_final.append(token)
    n = len(tokens_final)
    if n>3:
        for i in range(0,n-3):
            print(tokens_final[i]+' '+tokens_final[i+1]+' '+tokens_final[i+2]+' '+tokens_final[i+3]+'\t1')
