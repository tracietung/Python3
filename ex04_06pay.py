# Exercise 4.6
# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime
# and create a function called computepay which takes two parameters (hours and rate).

def computepay(hours, rate):
    maxi_hours = 40
    
    if hours > maxi_hours:
        basic_pay = maxi_hours * rate
        over_pay = (hours - maxi_hours) * 1.5 * rate
        pay = basic_pay + over_pay
    else:
        pay = hours * rate
        
    return pay

try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))

except:
    exit('Error, not a sufficient number.')

pay = computepay(hours, rate)
print('Pay:', pay)
