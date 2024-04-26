
"""

Bryce Chesley

This program gets information from the user and tells them the volume of thier
tires based on the information they give us, displaying thier tire's volume rounded.

the formula for calculating the volume of a tire:
v =(π*w^2 *a(w*a+2,540*d))/10,000,000,000

v is the volume in liters
π is pi
w is the width of the tire
d is the diameter of the wheel in inches
a is the aspect ratio of the tire


"""
import math
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
timestamp = datetime.now()



def volume(w, r, d): #<--- parameters
    return (math.pi* w ** 2 *r*(w * r + 2540 *d)) / 10000000000




width = float(input('enter the width of the tire in mm: '))
ratio = float(input('Enter the aspect ratio of the tire: '))
diameter = float(input('enter the diameter of the wheel in inches: '))

v = volume(width, ratio, diameter)# <--- arguments

try:
    file = open('volumes.txt', "a")
    file.write(f'\n{timestamp:%Y-%m-%d} ')
    file.write(f'Width: {width} ')
    file.write(f'Ratio: {ratio} ')
    file.write(f'Diameter: {diameter} ')
    file.write(f'Volume: {v:.2f} ')
    file.close()
except OSError:
    print('We were unable to append volumes.txt')




print(f'The aproximate volume of your tire is {v:.2f}')

buy = input('Would you like to buy tires in your specified size? [y/n]: ').lower()

if buy == "y":
    phone = input('Please Enter your phone number so we can contact you about your tires: ')
    try:
        file = open('volumes.txt', "a")
        file.write(f'y, {phone}')
        file.close()
    except OSError:
        print('We were unable to append volumes.txt')
else:
    try:
        file = open('volumes.txt', "a")
        file.write(f'n')
        file.close()
    except OSError:
        print('We were unable to append volumes.txt')


