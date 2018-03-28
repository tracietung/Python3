# Exercise 10.3
# Write a program that reads a file and prints the letters in decreasing order of
# frequency. Your program should convert all the input to lower case and only count
# the letters a-z. Your program should not count spaces, digits, punctuation, or
# anything other than the letters a-z. Find text samples from several different languages
# and see how letter frequency varies between languages.


fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be open', fname)
    exit()

import string  # import package/module
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation)) # delete punctuation
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.rstrip().lower()
    line = line.split()
    for words in line:
        word = list(words)
        for letter in word:
            if letter not in counts:
                counts[letter] = 1
            else:
                counts[letter] += 1

lst = list()
for l, freq in counts.items():
    lst.append((freq, l))

lst = sorted(lst, reverse=True)

for freq, l in lst:
    print(freq, l)


## Method 2: Regular Expressions
## printing top 10:

import re

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be open', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip().lower()
    letters = re.findall('[a-z]', line)
    for singleletter in letters:
        if singleletter not in counts:
            counts[singleletter] = 1
        else:
            counts[singleletter] += 1

lst = list()
for l, freq in counts.items():
    lst.append((freq, l))

lst = sorted(lst, reverse=True)

for freq, l in lst[:10]:
    print(freq, l)
