# Ch7 Exercise 2: Write a program to prompt for a file name,
# and then read through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475


fname = input('Enter a file name: ')
fhand = open(fname)
count = 0
total = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence: '):
        count +=1
        index = line.find(':')
        extract = line[index+2:]
        total += float(extract)
print('Average spam confidence: ', total/count)
