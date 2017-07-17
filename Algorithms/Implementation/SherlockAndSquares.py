# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import ceil, floor
def count_square(a, b):
    count = (int)(floor(pow(b, 0.5))- ceil(pow(a,0.5)))+1;
    print count
        
x = input()
for i in range(x):
    a, b = raw_input().split()
    count_square(int(a),int(b))
