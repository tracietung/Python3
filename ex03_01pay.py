# Exercise 3.1

hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
if hours > 40:
    pay1 = 40 * rate
    pay2 = (hours - 40) * (1.5 * rate)
    pay = pay1 + pay2
    print('Pay:', pay)

elif hours <= 40:
    pay3 = hours * rate
    print('Pay:', pay3)
