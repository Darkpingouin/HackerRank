# Enter your code here. Read input from STDIN. Print output to STDOUT
n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
price = map(int,raw_input().strip().split(' '))
bill = raw_input()
bill = int(bill)

total = 0
for x in range(n):
    if (x != k):
        total += price[x]
total /= 2
if (total == bill):
    print "Bon Appetit"
else:
    print bill - total
