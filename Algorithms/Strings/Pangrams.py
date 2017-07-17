# Enter your code here. Read input from STDIN. Print output to STDOUT
phrase = raw_input().lower()
alpha = "abcdefghijklmnopqrstuvwxyz"
for letter in alpha:
    if not(letter in phrase):
        print "not pangram"
        exit()
print "pangram"
