# ch4 vending machine - simple

def validate_inp(msg):
    try:
        entervalue = int(input(msg))
    except:
        exit('Enter integers only')
    if entervalue < 0:
        exit('Enter POSITIVE integers only')
    else:
        return entervalue


if __name__ == '__main__':

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

    amount = validate_inp('How many would you like to purchase? ')
    total = value * amount
    print('Your total is:', total)

    quarter = validate_inp('How many quarters do you want to insert? ')
    onedollar = validate_inp('How many one-dollar bills do you want to insert? ')
    changes = (quarter * 0.25 + onedollar) - total
    if changes < 0:
        print('Not a sufficient amount')
    else:
        print('Your changes:', changes)
