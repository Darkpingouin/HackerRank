#!/bin/python

import sys


s = raw_input().strip()
total = 1
for l in s:
    if l >= 'A' and l <= 'Z':
        total+=1
print total
