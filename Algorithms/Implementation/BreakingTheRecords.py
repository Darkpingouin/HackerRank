#!/bin/python

import sys

def getRecord(s):
    # Complete this function
    maxp = s[0]
    minp = s[0]
    tmax = 0
    tmin = 0
    for score in s:
        if (score < minp):
            minp = score
            tmin += 1
        elif (score > maxp):
            maxp = score
            tmax += 1
    print tmax, tmin
n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
getRecord(s)
