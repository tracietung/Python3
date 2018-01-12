# ch5 vending machine - loop

print('Healthy candy bar: $1.75 each.')
while True:
    try:
        count = int(input('How many would you like to purchase? '))
    except:
        print('Invalid input. Enter POSITIVE integers only')
        continue

    if count > 0:
        total = count * 1.75
        break

print('Your total is', total)
print('''Enter ".05" for a nickel;
".10" for a dime;
".25" for a quarter;
 or "1" for 1.00 dollar bill''')


sumup = 0
while True:
#    inp_money = float(input('Insert a value per time: '))
    for value in [.05, .10, .25, 1]:
        inp_money = input('Insert a value per time: ')
        try:
            fmoney = float(inp_money)
        except:
            print('Enter ".05", ".10", ".25" or "1" only')
            continue
        if fmoney == .05 or fmoney ==.10 or fmoney ==.25 or fmoney == 1:
            break
        else:
            print('Enter ".05", ".10", ".25" or "1" only')
            continue
    sumup = sumup + fmoney
    print(sumup)
    if sumup >= total:
        break

changes = sumup - total

quarter = changes // .25
quarter_remain = changes % .25
dime = quarter_remain // .10
dime_remain = quarter_remain % .10
nickel = dime_remain // .05
nickel_remain = dime_remain % .05

print('Your changes: {} quarters, {} dimes, and {} nickels'.format(quarter, dime, nickel) )
