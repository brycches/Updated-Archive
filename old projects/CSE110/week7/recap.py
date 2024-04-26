"""

this is how range works:
range(end) == range(0, end)
range(start, end)
range(start, end, increment)


this is how the for loop works
for [variable] in [list]:
this is a variable declaration

for color in colors
ex: for (this is a loop, it will do what is after it as many times as there are numbers in the index) color = [the current number of the index this l;oop is looking at] in colors

"""

numbers = range(1, 11)

#index ->   0       1       2
colors = ['Red', 'White', 'Blue'] #this is a list aka an array

print(colors[1])

print(range(1, 10, 1))

for num in numbers:
    print(num)

for color in colors:
    print(color)

for i, color in enumerate(colors):
    print(f'index {i} is {color} <=> {colors[i]}')