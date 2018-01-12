# ch5 exercise2
# Write another program that prompts for a list of numbers as above and at the
# end prints out both the maximum and minimum of the numbers instead of the average.

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
    count += 1

print('You have entered {} numbers; they are {}'.format(count, mylist))
print('You have entered {} numbers; they are {}'.format(len(mylist), mylist))  # built-in function

x_largest = mylist[0]
x_smallest = mylist[0]

for item in mylist:
    if item > x_largest:
        x_largest = item
    elif item < x_smallest:
        x_smallest = item

print('Largest: {} Smallest: {}'.format(x_largest, x_smallest))
print('Largest: {} Smallest: {}'.format(max(mylist), min(mylist)))  # built-in function
