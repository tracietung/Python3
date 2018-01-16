# ch5 vending machine - loop

# decide price
def get_price(selection):
    price = 2.25
    if selection == 'a':
        price = 1.75
    elif selection == 'b':
        price = 1.50
    return price


def get_total():
    while True:
        try:
            count = int(input('How many would you like to purchase? '))
        except:
            print('Invalid input. Enter POSITIVE integers only')
            continue
        if count > 0:
            return get_price(selection) * count
            break


def addmore():
    while True:
        add = input('Do you want to add more items? Enter "y" for yes, or enter "done": ')
        if add == 'done':
            return 'done'
        elif add == 'y':
            return 'y'
        else:
            print('Enter "y" or "done" only')
            continue


# main program

print('Enter "a" for Healthy candy bar: $1.75 each')
print('Enter "b" for Decaf Coke: $1.50 each')
print('Enter "c" for Squid jerky: $2.25 each')


subtotal = 0
while True:
    selection = input('Select the product. Enter "a", "b", or "c" only: ')
    if selection == 'a' or selection == 'b' or selection == 'c':
        subtotal += get_total()
        print('Your current total is', subtotal)
        addinp = addmore()
        if addinp == 'done':
            break
        elif addinp == 'y':
            continue
        break
    else:
        print('Enter "a", "b", or "c" only')
        continue

print('''Enter ".05" for a nickel;
".10" for a dime;
".25" for a quarter;
 or "1" for 1.00 dollar bill''')

sumup = 0
while True:
    while True:
        inp_money = input('Insert a value per time: ')
        fmoney = float(inp_money)
        if fmoney == .05 or fmoney == .10 or fmoney == .25 or fmoney == 1:
            break
        else:
            print('Enter ".05", ".10", ".25" or "1" only')
            continue
    sumup += fmoney
    rounded_sum = round(sumup, 2)
    print(rounded_sum)
    if rounded_sum >= subtotal:
        break

# give changes
changes = rounded_sum - subtotal

quarter = changes // .25
quarter_remain = changes % .25
dime = quarter_remain // .10
dime_remain = quarter_remain % .10
nickel = dime_remain // .05
nickel_remain = dime_remain % .05

print('Your changes: {} quarters, {} dimes, and {} nickels'.format(quarter, dime, nickel) )
