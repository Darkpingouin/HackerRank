#!/bin/python

import sys


n = int(raw_input().strip())
height = map(int,raw_input().strip().split(' '))

maxh = 0
total = 0
for i in range(n) :
    if (height[i] > maxh):
        maxh = height[i]
        
for j in range(n) :
    if (height[j] == maxh):
        total += 1
        
        
print total
