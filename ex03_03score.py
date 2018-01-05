# Exercise 3.3

print('What was your score of the class you recently took? Enter a score between 0.0 and 1.0.')
scr = input('Enter score: ')
try:
     s = float(scr)
except:
    s = -1

if s >= 0.9 and s < 1.0:
    print('A')
elif s >= 0.8 and s < 0.9:
    print('B')
elif s >= 0.7 and s < 0.8:
    print('C')
elif s >= 0.6 and s < 0.7:
    print('D')
elif s < 0.6 and s > 0.0:
    print('F')
else:
    print('Bad score')
