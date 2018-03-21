# Exercise 10.1
# Revise a previous program as follows: Read and parse the "From" lines and pull
# out the addresses from the line. Count the number of messages from each person
# using a dictionary.

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

emails = list()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'): continue
    elif line.startswith('From'):
        words = line.split()
        emails.append(words[1])

counts = dict()
for address in emails:
    counts[address] = counts.get(address, 0) +1
print(counts)

lst = list()
for email, count in counts.items():
    lst.append((count, email))
lst = sorted(lst, reverse=True)
print(lst)

for count, email in lst[:1]:
    print (email, count)
