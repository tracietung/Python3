# Exercise 10.2
# This program counts the distribution of the hour of the day for each of the messages.
# You can pull the hour from the "From" line by finding the time string and then splitting
# that string into parts using the colon character. Once you have accumulated the counts
# for each hour, print out the counts, one per line, sorted by hour as shown below.


fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be open', fname)
    exit()

dayhour = list()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'): continue
    elif line.startswith('From'):
        words = line.split()
        hours = words[5].split(':')
        dayhour.append(hours[0])
print(dayhour)

counthours = dict()
for number in dayhour:
    counthours[number] = counthours.get(number, 0) +1

lst = sorted(counthours.items())

for hour, count in lst:
    print (hour,count)
