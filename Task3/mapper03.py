#!/usr/bin/python3

"""
Created on Tue Oct 10 17:57:02 2017
@author: kotsabo
"""

import sys
import re

max_bytes, max_tokens = 0, 0

for line in sys.stdin:
    tokens_final = list()
    number_bytes = len(line)-1
    tokens = re.split('\n| |\t|\r|\f',line)
    for token in tokens:
        if token != '':
            tokens_final.append(token)
    number_tokens = len(tokens_final)
    if number_bytes > max_bytes:
        max_bytes = number_bytes
    if number_tokens > max_tokens:
        max_tokens = number_tokens

print(str(max_bytes) + ' ' + str(max_tokens))
