# Ch8_Exercise 6: Rewrite the program that prompts the user for a list
# of numbers and prints out the maximum and minimum of the numbers
# at the end when the user enters "done". Write the program to store
# the numbers the user enters in a list and use the max() and min() functions


mylist = list()
while True:
    inp = input('Enter a number each time, when you finish, enter "done". Enter a number: ')
    if inp == 'done': break
    try:
        message = float(inp)
        mylist.append(message)
    except:
        print('Enter a "number" each time')

print('Maximum:', max(mylist))
print('Minimum:', min(mylist))
