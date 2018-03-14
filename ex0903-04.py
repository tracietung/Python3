# Ex0903
# Exercise 3: Write a program to read through a mail log, build a histogram using
# a dictionary to count how many messages have come from each email address,
# and print the dictionary.


# Ex0904
# Add code to the above program to figure out who has the most messages in the file.



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
        words = line.split()
        authors.append(words[1])

counts = dict()
for email in authors:
    counts[email] = counts.get(email, 0) +1
print(counts)

bigcount = None        # Ex0904
bigemail = None
for email,count in counts.items():
    if bigemail is None or count > bigcount:
        bigemail = email
        bigcount = count

print(bigemail, bigcount)
