#!/bin/python

import sys


n = int(raw_input().strip())
grid = []
grid_i = 0
for grid_i in xrange(n):
    grid_t = str(raw_input().strip())
    grid.append(grid_t)
for x in range(n):
    for y in range (n):
        if (x != 0 and x != n-1 and y != 0 and y!= n-1):
            tmp = grid[x][y]
            up = grid[x-1][y]
            down = grid[x+1][y]
            left = grid[x][y-1]
            right = grid[x][y+1]
            if (tmp > up and tmp > down and tmp > left and tmp > right):
                sys.stdout.write('X')
            else:
                sys.stdout.write(grid[x][y])  
        else:
         sys.stdout.write(grid[x][y])  
    sys.stdout.write('\n')  
