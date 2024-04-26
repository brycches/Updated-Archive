import math
lengths = float(input('what is the length of one of the sides of your square? '))

areas = lengths**2

print (f'your square has an area of: {areas}')


widthr = float(input("what is the length of one of your rectangl's sides?" ))
lengthr = float(input("what is the length of the other side of your rectangle? "))

arear = widthr * lengthr

print(f"your rectangle has an area of: {arear}")

radius = float(input('What is the radius of your circle? '))

pi = math.pi

areac = pi * (radius**2)

print(f'your circle has an area of: {areac:.3g}')


lengtha = float(input("what is the length of your side? "))

circle = pi * (lengtha**2)

print(f'the area of your circle with a radius of {lengtha} is: {circle:.3g}')

square = lengtha**2

print(f'the area of your square with a side length of {lengtha} is: {square:.3g}')

cube = lengtha**3

print(f'the volume of your cube with a side length of {lengtha} is: {cube:.3g}')

