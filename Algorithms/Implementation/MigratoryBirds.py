#!/bin/python

import sys


n = int(raw_input().strip())
types = map(int, raw_input().strip().split(' '))
# your code goes here

total = [0, 0, 0, 0, 0]
for bird in range(n):
    total[types[bird]-1] += 1
print total.index(max(total)) + 1
