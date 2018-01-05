# Exercise 3.1

hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
maxi_hours = 40
if hours > maxi_hours:
    pay1 = maxi_hours * rate  # pay of 40 hours
    pay2 = (hours - maxi_hours) * (1.5 * rate)  # pay of hours worked above 40 hours
    pay = pay1 + pay2
    print('Pay:', pay)

elif hours <= maxi_hours:
    pay3 = hours * rate  # pay of hours less than and equal to 40 hours
    print('Pay:', pay3)
