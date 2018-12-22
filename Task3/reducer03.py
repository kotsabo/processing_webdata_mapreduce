#!/usr/bin/python3

import sys

max_bytes, max_tokens = 0, 0

for line in sys.stdin:
    if line.strip() != '':
       temp_max_bytes, temp_max_tokens = line.strip().split(' ')
       temp_max_bytes = int(temp_max_bytes)
       temp_max_tokens = int(temp_max_tokens)
       if temp_max_bytes > max_bytes:
             max_bytes = temp_max_bytes
       if temp_max_tokens > max_tokens:
             max_tokens = temp_max_tokens

print(str(max_bytes) + ' ' + str(max_tokens))
