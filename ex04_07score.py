# Exercise 3.3

print('What was your score of the class you recently took? \
Enter a score between 0 and 1.0.')

try:
    scr = float(input('Enter score: '))
    def computegrade(scr):
        if 0.9 <= scr < 1.0:
            print('A')
        elif 0.8 <= scr < 0.9:
            print('B')
        elif 0.7 <= scr < 0.8:
            print('C')
        elif 0.6 <= scr < 0.7:
            print('D')
        elif 0.5 <= scr < 0.6:
            print('F')
        elif 0 <= scr <0.5:
            print('Bad score')
        else:
            print('Out of range')

except:
    exit('Not a sufficient score')


computegrade(scr)
