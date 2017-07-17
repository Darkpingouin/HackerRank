#!/bin/python

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
c.sort()
total = 0
sock = c[0]
add = 0
for x in range(n):
    if c[x] == sock:
        add+=1
    else:
        sock = c[x]
        if (add % 2) == 0 and add != 0:
            total += (add / 2)
        add -= 1
        if (add % 2) == 0 and add != 0:
            total += (add / 2)
        add = 1
if (add % 2) == 0 and add != 1:
    total += (add / 2)
add -= 1
if (add % 2) == 0 and add != 1:
    total += (add / 2)  
print total

    
