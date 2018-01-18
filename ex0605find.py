# Ch6 Exercise 5: Take the following Python code that stores a string:`

# str = 'X-DSPAM-Confidence:0.8475'

# Use find and string slicing to extract the portion of the string after
#the colon character and then use the float function to convert the extracted
#string into a floating point number.



string = 'X-DSPAM-Confidence: 0.8475'
index = string.find(':')
print (index)
extract = string[index+2:]
print(float(extract))

# .strip - chop the characters at the leaing and tailing positions.

string_sp = ' X-DSPAM-Confidence: 0.8475 '
strip_spaces = string_sp.strip()
print(strip_spaces)

#test = 'www.example.com'.strip('cmowz.')
#print(test)

test = '#$...X-DSPAM-Confidence: 0.8475.com:'
strip_s = test.strip('#$.:')
print(strip_s)

#replace
replace_e = test.replace('e', 'y',2)
print(replace_e)
