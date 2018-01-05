# Exercise 3.2

hours = input('Enter Hours: ')
try:
    h = int(hours)
except:
    h = -1

if h == -1:
    print('Error, please enter numeric input')
else:
    rate = input('Enter Rate: ')
    try:
        r = int(rate)
    except:
        r = -1

    if r == -1:
        print('Error, please enter numeric input')
    else:
        if h > 40:
            pay1 = 40 * float(rate)
            pay2 = (h - 40) * 1.5 * float(rate)
            pay = pay1 + pay2
            print('Pay:', pay)
        elif h <= 40:
            pay3 = h * float(rate)
            print('Pay:', pay3)
