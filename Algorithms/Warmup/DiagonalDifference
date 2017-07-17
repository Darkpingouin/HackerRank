#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
i = 0
d1 = 0
d2 = 0
for x in range(n):
  d1 += a[x][i]
  i+=1
i = n - 1
for x in range(n):
  d2 += a[x][i]
  i-=1

total = d1 - d2
if total < 0:
    total *= -1
print total
        
