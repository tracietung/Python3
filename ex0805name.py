# Ch8 - Ex05
# Exercise 5: Write a program to read through the mail box data and
# when you find line that starts with "From", you will split the
# line into words using the split function. We are interested in who
# sent the message, which is the second word on the From line.

#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

# You will parse the From line and print out the second word for each
# From line, then you will also count the number of From (not From:)
# lines and print out a count at the end.


fname = input('Enter a file name: ')
fhand = open(fname)
count = 0
emails = list()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'): continue
    elif line.startswith('From'):
        words = line.split()
        print(words[1])
        emails.append(words[1])
        count += 1
print('There were {} lines in the file with From as the first word.'.format(count))

#### extended practice:

def oneline(i):
    for s in i:
        print(s)

new_count = 0
new_emails = list()
for i in emails:
    if i in new_emails: continue
    new_emails.append(i)
    new_count+=1
new_emails.sort()
print('There were {} senders in the file. They are: '.format(new_count))
final_list = oneline(new_emails)
print(final_list)


#for s in new_emails:
#    print(s)
