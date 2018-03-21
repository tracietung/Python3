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

import string

counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.strip().lower()
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
