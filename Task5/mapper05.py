#!/usr/bin/python3

"""
Created on Tue Oct 10 23:08:12 2017
@author: kotsabo
"""

import sys
import bisect

max_array = [0]*25
sentences_array = [""]*25


for line in sys.stdin:
    sentence, count = line.split('\t')
    count = int(count)
    bisect.insort(max_array, count)
    index = max_array.index(count)
    max_array.pop(0)
    sentences_array.insert(index, sentence)
    sentences_array.pop(0)

for i in range(0,25):
    print(sentences_array[24-i]+'\t'+str(max_array[24-i]))
