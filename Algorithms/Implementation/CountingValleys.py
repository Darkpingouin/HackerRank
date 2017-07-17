# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
steps = raw_input().strip()

height = 0
total = 0
start = -1
for x in range(n):
    
    if (steps[x] == 'U'):
        height += 1
        if height < 0 and start < 0:
            start = height
    else:
        height -= 1
        if (height == start):
            total += 1
            start = -1
print total
