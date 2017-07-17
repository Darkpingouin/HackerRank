# Enter your code here. Read input from STDIN. Print output to STDOUT

def reversed(day):
    return int(day[::-1])

def isBeautiful(day, yad, k):
    return (abs(day - yad) % k) == 0

i, j, k = raw_input().strip().split();

i, j, k = int(i), int(j), int(k)
total = 0
for day in range(i, j):
    if isBeautiful(day, reversed(str(day)), k):
        total += 1
print total
