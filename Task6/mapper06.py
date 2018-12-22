#!/usr/bin/python3

"""
Created on Wed Oct 11 20:49:21 2017
@author: kotsabo
"""

import sys

key, four_token, count = None, None, 0
dictionary = dict()

for line in sys.stdin:
    line.strip()
    four_token, count = line.split('\t')
    count = int(count)
    tokens = four_token.split()
    key = tokens[0]+' '+tokens[1]+' '+tokens[2]
    final_line = key + '\t' + str(count)
    print(final_line)
