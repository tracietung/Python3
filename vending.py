# ch4 vending machine - simple

print('''Candy bar $2.25: enter "a";
Chips $3.00: enter "b";
Beef jerky $3.50: enter "c"''')
product = input('Select a product, enter "a", "b", or "c": ')

if product == 'a':
    value = 2.25
elif product == 'b':
    value = 3.00
elif product == 'c':
    value = 3.50
else:
    exit('Enter "a" or "b" or "c" only')
try:
    quarter = int(input('How many quarters do you want to insert? '))
except:
    exit('Enter integers only')

if quarter < 0:
    exit('Enter POSITIVE integers only')
else:
    try:
        onedollar = int(input('How many one-dollar bills do you want to insert? '))
    except:
        exit('Enter integers only')
    if onedollar < 0:
        print('Enter POSITIVE integers only')
    else:
        money = (quarter * 0.25 + onedollar) - value
        print(money)
