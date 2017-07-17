#!/bin/python

import sys


def isfact(numbers, x):
    for nb in numbers:
        if(x % nb != 0):
            return False
    return True

def hasfact(numbers, x):
    for nb in (numbers):
        if (nb % x != 0):
            return False
    return True

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))

total = 0
for x in range(1, min(b) + 1):
    if (isfact(a, x) and hasfact(b, x)):
        total += 1
print total
