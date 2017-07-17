#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))


totala = 0
totalo = 0

#print "distance", s, t
for i in range(m):
    #print "apple", a + apple[i]
    if (a + apple[i]) >= s and (a + apple[i]) <= t:
        totala += 1
        
for j in range(n):
    #print "orange", b + orange[i]
    if (b + orange[j]) >= s and (b + orange[j]) <= t:
        totalo += 1

print totala
print totalo
