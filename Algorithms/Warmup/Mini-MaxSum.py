#!/bin/python

import sys


a,b,c,d,e = raw_input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
ar = [a,b,c,d,e]
ar.sort()
smin = ar[0] + ar[1] + ar[2] + ar[3]
smax = ar[1] + ar[2] + ar[3] + ar[4]
print smin, smax
