
import math
"""

v =(π*w^2 *a(w*a+2,540*d))/10,000,000,000

v is the volume in liters
π is pi
w is the width of the tire
d is the diameter of the wheel in inches
a is the aspect ratio of the tire


"""




def volume(w, r, d): #<--- parameters
    #no
    return (math.pi* w ** 2 *r*(w * r + 2540 *d)) / 10000000000




width = float(input('enter the width of the tire in mm: '))
ratio = float(input('Enter the aspect ratio of the tire: '))
diameter = float(input('enter the diameter of the wheel in inches: '))

v = volume(width, ratio, diameter)# <--- arguments
print(f'{v:.2f}')