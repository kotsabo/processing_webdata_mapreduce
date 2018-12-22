#!/usr/bin/python3

import sys

key, key2, previous_key,  total = None, None, None, 0

for line in sys.stdin:
    key2, count = line.strip().split('\t')
    count = int(count)
    if key2!=key:
        if total==1:
                print(key)
        key, total, previous_key = key2, count, key
    else:
        total += count

if key2 != previous_key:
    print(key2)
