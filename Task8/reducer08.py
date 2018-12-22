#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Created on Sun Oct 15 02:40:07 2017

@author: kotsabo
"""

import sys

average, next_average, student_id = None, None, None
students = list()
flag = False

for line in sys.stdin:
    line = line.strip()
    next_average, student_id = line.split('-')

    if next_average != average and average != None:
        if not flag:
            flag = True
            for student in students:
                print('names: ' + student + ' scores: ' + average)

    students.append(student_id)
    average = next_average
    