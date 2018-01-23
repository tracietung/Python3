# Ch7 Exercise#3


fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('Subject: '):
        count +=1

print('There were {} subject lines in {}'.format(count, fname))
