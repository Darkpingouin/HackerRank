#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    div = 0
    nstr = str(n)
    for l in nstr:
        if (int(l) != 0 and  n % int(l) == 0):
            div += 1
    print div
