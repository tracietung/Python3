# Ch11 Exercise 1
# Exercise 1: Write a simple program to simulate the operation of the grep command
# on Unix. Ask the user to enter a regular expression and count the number of lines
# that matched the regular expression:

import re

fhand = open('mbox.txt')

entered = input('Enter a regular expression: ')
count = 0
for line in fhand:
    line = line.rstrip()
    if re.search(entered, line):
        count = count + 1
    else:
        continue

print('mbox.txt. had {} lines that matched {}' .format(count, entered))
