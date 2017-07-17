#!/bin/python

import sys


h = map(int, raw_input().strip().split(' '))
word = raw_input().strip()
maxl = 0
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
l = list(set(word))
for le in l:
    if (h[letters.index(le)] > maxl):
        maxl = h[letters.index(le)]
        
print maxl * len(word)
