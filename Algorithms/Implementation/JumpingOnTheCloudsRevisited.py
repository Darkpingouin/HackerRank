#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
c = map(int,raw_input().strip().split(' '))

E = 99
i = 0
cloud = i + k % n
if c[cloud] == 1:
    E-=2
while(cloud != 0):
    cloud = ((cloud + k) % n )
    E -= 1
    if c[cloud] == 1:
        E -= 2
print E
