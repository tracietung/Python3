#### Ch9: Exercise 1
# Write a program that reads the words in words.txt and
# stores them as keys in a dictionary. It doesn't matter what the values are.
# Then you can use the in operator as a fast way to check whether a string is
# in the dictionary.


inp = input('Enter the file: ')
fhand = open(inp)
fline = fhand.read()    # .read() print the content in its original layout
print(fline)
words = fline.split()     # make those words into a list

wordsdict= dict()
for word in words:
    wordsdict[word] = ''    # this just for printing out the words, make the words to be kys
print(wordsdict)
print('But' in wordsdict)
