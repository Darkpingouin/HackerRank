#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
height = map(int, raw_input().strip().split(' '))
# your code goes here
maxx = 0
for x in range(n):
    if (height[x] > maxx):
        maxx = height[x]

if (maxx > k):
    print maxx - k
else:
    print 0
