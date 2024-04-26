import math

def compute_area_square(lengths):
    return compute_area_rectangle(lengths, lengths)

def compute_area_rectangle(widthr, lengthr):
    return widthr * lengthr

def compute_area_circle(radius):
    pi = math.pi
    return pi * (radius**2)

answer = ''

while answer != 'quit':
    try:
        answer = input('what shape would you like to know the area of (square, rectangle, or circle)? You can also type quit to quit: ')
    except:
        print('please enter a shape, or type quit to quit')
        continue
    if answer.lower() == 'quit':
        break
    elif answer.lower() == 'square':
        lengths = float(input('what is the length of one of the sides of your square? '))
        areas = compute_area_square(lengths)
        print(f'your square has an area of: {areas}')
        continue
    elif answer.lower() == 'rectangle':
        widthr = float(input("what is the length of one of your rectangle's sides?" ))
        lengthr = float(input("what is the length of the other side of your rectangle? "))
        arear = compute_area_rectangle(widthr, lengthr)
        print(f"your rectangle has an area of: {arear}")
        continue
    elif answer.lower() == 'circle':
        # radius = float(input('What is the radius of your circle? '))
        areac = compute_area_circle(float(input('What is the radius of your circle? ')))
        # areac = compute_area_circle(radius)
        print(f'your circle has an area of: {areac:.3g}')
        continue
    else:
        print('please enter a valid shape, or type quit to quit')
        continue





# lengths = float(input('what is the length of one of the sides of your square? '))

# # areas = lengths**2
# areas = compute_area_square(lengths)

# print (f'your square has an area of: {areas}')


# widthr = float(input("what is the length of one of your rectangle's sides?" ))
# lengthr = float(input("what is the length of the other side of your rectangle? "))

# # arear = widthr * lengthr
# arear = compute_area_rectangle(widthr, lengthr)

# print(f"your rectangle has an area of: {arear}")

# radius = float(input('What is the radius of your circle? '))

# # pi = math.pi

# # areac = pi * (radius**2)
# areac = compute_area_circle(radius)

# print(f'your circle has an area of: {areac:.3g}')



# lengtha = float(input("what is the length of your side? "))

# circle = pi * (lengtha**2)

# print(f'the area of your circle with a radius of {lengtha} is: {circle:.3g}')

# square = lengtha**2

# print(f'the area of your square with a side length of {lengtha} is: {square:.3g}')

# cube = lengtha**3

# print(f'the volume of your cube with a side length of {lengtha} is: {cube:.3g}')

