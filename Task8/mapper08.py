#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 01:59:48 2017

@author: kotsabo
"""

import sys
import re

for line in sys.stdin:
    line = line.strip()
    key, values = line.split(' -->')
    
    values = re.split('\(|\)',values)

    final_values = list()
    for value in values:
        if value != '' and value != ' ':
            final_values.append(value)
            
    if len(final_values) > 3:
        summary = 0
        for value in final_values:
            value, lesson = value.split(',')
            summary += int(value)
        
        print(str(round(summary/len(final_values),2))+'-'+key)

