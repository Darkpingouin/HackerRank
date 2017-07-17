#!/bin/python

import sys


N = int(raw_input().strip())

if N % 2 == 1:
    print "Weird"
elif N % 2 == 0 and ((N >= 2 and N <= 5) or (N > 20)):
    print "Not Weird"
else:
    print "Weird"
