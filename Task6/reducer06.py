#!/usr/bin/python3

"""
Created on Thu Oct 12 14:11:12 2017
@author: kotsabo
"""

import sys
import math

def minus_xlog2x(x):
    return -x*math.log2(x)

def entropy(total_list,summary):
    entropy = 0
    for count in total_list:
        entropy += minus_xlog2x(count/summary)
    return entropy

value, key, new_key= 0, None, None
summary = 0
total_list = list()

for line in sys.stdin:
    new_key, value = line.split('\t')
    value = int(value)

    if new_key != key and key != None:
        print(key + '\t' + str(round(entropy(total_list,summary),4)))
        summary = 0
        total_list = list()

    key = new_key
    summary += value
    total_list.append(value)

print(key + '\t' + str(round(entropy(total_list,summary),4)))