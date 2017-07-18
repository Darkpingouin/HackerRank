#!/bin/python

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
moves = -1
i = 0
while i < len(c):
    if (i + 2 < len(c) and (c[i+2] != 1)):
            i+=2
            moves+=1
    else:
        i+=1
        moves+=1
print moves  
