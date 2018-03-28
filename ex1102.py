# Ch11: Exercise 2

# Write a program to look for lines of the form:
# `New Revision: 39772`
# and extract the number from each of the lines using a regular expression and
# the findall() method. Compute the average of the numbers and print out the average.

import re
fname = input('Enter file: ', )
fhand = open(fname)
total = 0
count = 0
for line in fhand:
    line = line.rstrip()
    exnumber = re.findall('^New Revision: ([0-9].+)', line)
    if len(exnumber) > 0:
        for i in exnumber:
            newnumber = float(i)
            total = total + newnumber
            count = count + 1

average = total / count

print(average)
