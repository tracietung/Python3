#ch5 exercise2
#Write another program that prompts for a list of numbers as above and at the
#end prints out both the maximum and minimum of the numbers instead of the average.

print('Provide a list a number here; start to enter numbers')
print('Enter "done" when you entered all the numbers.')

count = 0
mylist = []
while True:
    inp_num = input('Enter a number: ')
    if inp_num == 'done':
        break
    try:
        finp = float(inp_num)
    except:
        print('Invalid value')
        continue
    mylist.append(finp)
    count = count + 1
print('You have entered {} numbers; they are {}' .format(count, mylist))

x_largest = None
for itervar in mylist:
    if x_largest is None or itervar > x_largest :
        x_largest = itervar

x_smallest = None
for itervar in mylist:
    if x_smallest is None or itervar < x_smallest:
        x_smallest = itervar

print('Largest:', x_largest, 'Smallest:', x_smallest)

#largest = max(mylist)
#smallest = min(mylist)
#print('Max:', largest, 'Min:', smallest)
