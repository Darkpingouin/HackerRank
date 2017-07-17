#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
pos = 0.0
neg = 0.0
zer = 0.0
for x in range(n):
    if (arr[x] > 0):
        pos+=1
    elif (arr[x] < 0):
        neg+=1
    else:
        zer += 1
pos /= n
neg /= n
zer /= n
print pos
print neg
print zer
