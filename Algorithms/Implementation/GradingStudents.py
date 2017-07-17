#!/bin/python

import sys

def solve(grades):
    # Complete this function
    for grade in grades:
        if grade < 38:
            print grade
        elif (grade + 1) % 5 == 0:
            print grade+1
        elif (grade + 2) % 5 == 0:
            print grade + 2
        else:
            print grade

n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)

