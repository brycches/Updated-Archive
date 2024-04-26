import math
#asking for the variables
radius = float(input('what is the radius of your perfectly cylendrical mug in inches? '))

height = float(input('what is the height of your perfectly cylendrical mug in inches? '))

cubic_inches = math.floor((math.pi * (radius**2)) * height)

print (f'your mug is {cubic_inches:.0f} cubic inches in volume')

oz = math.floor(cubic_inches * .554113)

print (f'or in other words it contains {oz:.0f} ounces')

cup = math.floor(oz / 8)

print(f'or in other words your perfectly cilindrical mug contains {cup:.0f} cups')

