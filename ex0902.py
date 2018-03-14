# Ex0902
# Exercise 2: Write a program that categorizes each mail message by which day of
# the week the commit was done. To do this look for lines that start with "From",
# then look for the third word and keep a running count of each of the days of the week.
# At the end of the program print out the contents of your dictionary
# (order does not matter).


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

wkdays = list()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'): continue
    elif line.startswith('From'):
        words = line.split()
        wkdays.append(words[2])

counts = dict()
for word in wkdays:
    counts[word] = counts.get(word, 0) +1
print(counts)


# is there anyway to dictionary the 2nd word in the line directly??
