# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()

# Print the day of the week for the user to see.
#print(day_of_week)
subtotal = 0
price = -1
while price != 0:
    price = float(input('What is the price of your item? '))
                  
    quantity = int(input('how many of that item are you purchasing? '))

    subtotal += price*quantity

subtotal = float(subtotal)
if day_of_week == 1 or day_of_week == 2:
    give_discount = True
else:
    give_discount = False

if give_discount == True and subtotal >= 50:
    total = (subtotal * .9) * 1.06
else:
    total = subtotal * 1.06

print (f'your total is {total:.2f}')