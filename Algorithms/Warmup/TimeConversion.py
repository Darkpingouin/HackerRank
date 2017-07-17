#!/bin/python

import sys


time = raw_input().strip()
a = False
if "PM" in time:
    a = True
time = time.replace('A', 'P').replace('PM', '').split(':')

if a:
    time[0] = int(time[0])
    if (time[0] < 12):
        time[0] += 12
else:
    if int(time[0]) == 12:
        time[0] = "00"
t = str(time[0]) + ":" + time[1] + ":" + time[2]
print t
