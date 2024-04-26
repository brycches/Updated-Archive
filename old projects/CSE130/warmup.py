import json

year = int(1971)

print(f'i was born in {year}')


name = input('what is your name? ')

print(f'your name is {name}')

year = int(input('what is your birth year? '))

age = 2023-year
print(f'you are {age} years old')

try:
    file = open("name.txt","w")
    file.write("Bryce Chesley")
    file.close()
except OSError:
    print("unable to write to name.txt")

try:
    file = open("name.txt","r")
    name = file.readline()
    print("The name is " + name)

    file.close()
except OSError:
    print("unable to read name.txt")


construct = {1: 'one',2: 'two',3: 'three','no':['i dont like lists', 'especially in dictionaries', 'which are wierd']}

unconstructed = json.dumps(construct)

try:
    file = open("data.json", "w")
    file.write(unconstructed)
    file.close()
except OSError:
    print('unable to write to data.json ')

try:
    file = open("data.json", "r")
    text2 = file.read()
    data2 = json.loads(text2)
    file.close()
except:
    print('unable to read data.json ')

print(f'{data2}')

array = [0,1,2,3,4,5,6,7,8,9]

for numbers in array:
    print(f'{numbers}')


print(f'{array[:3]}')
print(f'{array[-3:]}')
print(f'{array[3:7]}')

tuple_one = 1,1.1
print('tuple_one =', tuple_one)
print("tuple_one[0] =", tuple_one[0])
print("tuple_one[1] =", tuple_one[1])

tuple_two = "two", True, (2, 2+2j)
print("tuple_two =", tuple_two)
print("tuple_two[0] =", tuple_two[0])
print("tuple_two[1] =", tuple_two[1])
print("tuple_two[2] =", tuple_two[2])




