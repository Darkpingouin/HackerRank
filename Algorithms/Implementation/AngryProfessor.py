#!/bin/python

import sys


t = int(raw_input().strip())
for x in range(t):
    l1 = raw_input().split()
    nb = int(l1[0])
    k = int(l1[1])
    l2 = raw_input().split()
    p = 0
    r = 0
    for y in range(nb):
        if int(l2[y]) > 0:
            r += 1
    if (nb - r) < k:
        print "YES"
    else:
        print "NO"
