def validate_int_input(msg):
    try:
        currency_amt = int(input(msg))
    except:
        exit('Enter integers only')

    if currency_amt < 0:
        exit('Enter POSITIVE integers only')

    return currency_amt


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

    quarter = validate_int_input('How many quarters do you want to insert? ')
    one_dollar = validate_int_input('How many one_dollar bills do you want to insert? ')
    changes = (quarter * 0.25 + one_dollar) - value
    print(changes)
