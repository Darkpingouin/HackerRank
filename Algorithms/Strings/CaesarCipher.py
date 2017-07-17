#!/bin/python

import sys


n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())
result = ""
for i in range(n):
    if (s[i] >= 'A' and s[i] <= 'Z'):
        tmp = chr(ord(s[i]) + k % 26)
        if (tmp > 'Z'):
            tmp = chr(ord(tmp) - 26)
        result += tmp
    elif (s[i] >= 'a' and s[i] <= 'z'):
        tmp = chr(ord(s[i]) + k % 26)
        if (tmp > 'z'):
            tmp = chr(ord(tmp) - 26)
        result += tmp
    else:
        result += s[i]
print result
