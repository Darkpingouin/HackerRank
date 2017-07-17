#!/bin/python

import sys

def black(b, x, y, z):
    if (y + z < x):
        return b * (y + z)
    else:
        return b * x
    
def white(w, x, y, z):
    if (x + z < y):
        return w * (x + z)
    else:
        return w * y
    
    
def convert(b, w, x, y, z):
    total = 0
    total = black(b, x, y, z) + white(w, x, y, z)
    return total

t = int(raw_input().strip())
for a0 in xrange(t):
    b,w = raw_input().strip().split(' ')
    b,w = [long(b),long(w)]
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [long(x),long(y),long(z)]
    print convert(b, w, x, y, z)
