import math


print('Welcome to the velocity calculator. Please enter the following: ')

mass = float(input('what is the mass of the object in kilograms? '))

gravity = float(input('what is the Gravity of your planet (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))

time = float(input('what is the time since you dropped the object (in seconds)? '))

density = float(input('what is the density of the fluid the object is falling in? (1.3 kg/m^3 for air, 1000 kg/m^3 for water)? '))

area = float(input('what is the cross sectional area of projectile (in square meters)? '))

dragc = float(input("what is the drag constant (0.5 for sphere, 1.1 for cylinder falling on it's side. You could look it up for other shapes.) for your object? "))








drag = ((1/2) * density * area * dragc)

print (f'the drag of your object is {drag}')



velocity =(math.sqrt((mass * gravity)/drag) * (1-math.exp( -((math.sqrt(mass * gravity * drag)) / mass) * time)))

print (f'the velocity of your object after {time} seconds is {velocity} m/s')
