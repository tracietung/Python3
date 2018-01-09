# Exercise 3.2

try:
    hours = int(input('Enter Hours: '))
    rate = int(input('Enter Rate: '))
    maxi_hours = 40
    pay = hours * rate
    if hours > maxi_hours:
        basic_pay = maxi_hours * (rate)
        over_pay = (hours - maxi_hours) * 1.5 * (rate)
        pay = basic_pay + over_pay
        print('Pay:', pay)
except:
    exit('Error, please enter numeric input')
