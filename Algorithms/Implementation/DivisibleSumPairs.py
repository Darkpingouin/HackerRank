#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = raw_input().split()


total = 0
for i in range(n):
    for j in range(n):
        sum = (int(a[i]) + int(a[j]))
        if (i < j and (sum % k == 0)):
           total+=1
print int(total)
