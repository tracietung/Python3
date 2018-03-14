# Ex0905
# Exercise 5: This program records the domain name (instead of the address)
# where the message was sent from instead of who the mail came from (i.e.,
# the whole email address). At the end of the program, print out the contents of your dictionary.


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

authors = list()
for line in fhand:
    line = line.rstrip()
    if line.startswith('Author:'):
        atpos = line.find('@')
        host = line[atpos+1:]    # "one beyond the at-sign through the end".
        authors.append(host)

counts = dict()
for schoolhost in authors:
    counts[schoolhost] = counts.get(schoolhost, 0) +1
print(counts)
