#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

tmp = []
while len(arr) > 0:
    print len(arr)
    tmp = []
    m = min(arr)
    for x in range(len(arr)):
        arr[x] = arr[x] - m
    for x in range(len(arr)):
        if (arr[x] != 0):
           tmp.append(arr[x])
    arr = list(tmp)

