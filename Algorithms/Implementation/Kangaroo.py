#!/bin/python

import sys


x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

step1 = x1
step2 = x2
if (v1 > v2):
    while step1 < step2:
        step1 += v1
        step2 += v2
if (step1 == step2):
    print "YES"
else:
    print "NO"
    
